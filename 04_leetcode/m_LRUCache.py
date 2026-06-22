"""
Problem: LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
URL: 
Difficulty: [Medium]
Pattern: hash map..two pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None  # Links to the train car physically ahead of this one
        self.next = None  # Links to the train car physically behind this one


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()  # Our fast-pass map: lets us jump directly to any train car using its key
        self.head = Node(0, 0)  # Permanent "Front Gate" of the station. Most recent items park right after this.
        self.tail = Node(0, 0)  # Permanent "Back Gate" of the station. Oldest items sit right before this.

        # Initially, the station is empty, so the Front Gate and Back Gate hold hands directly
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        """
        Cuts a train car out of the line completely.
        It tells the car's left and right neighbors to bypass it and hold hands with each other.
        """
        prev_node = node.prev  # Identify who is standing to the left
        next_node = node.next  # Identify who is standing to the right

        prev_node.next = next_node  # Tell the left neighbor to point past 'node' to the right neighbor
        next_node.prev = prev_node  # Tell the right neighbor to point past 'node' to the left neighbor

    def insert(self, node: Node):
        """
        Squeezes a train car into the VIP slot right after the Front Gate (self.head).
        """
        # 1. Identify who is currently first in line so we don't drop them in the dark
        current_first = self.head.next

        # 2. Make the new node hold hands with its new left neighbor (the Front Gate)
        self.head.next = node
        node.prev = self.head

        # 3. Make the new node hold hands with its new right neighbor (the old first node)
        node.next = current_first
        current_first.prev = node

    def get(self, key: int) -> int:
        # Check our fast-pass map to see if the item exists
        if key in self.cache:
            node = self.cache[key]  # Jump straight to the physical train car

            # Since this item was just requested, it's now the "Most Recently Used"
            # Refresh its status by pulling it out of line and sending it to the front
            self.remove(node)
            self.insert(node)

            return node.value  # Deliver the requested data

        # If the key isn't anywhere in our map, the item doesn't exist
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # --- CASE 1: Updating an item we already have ---
            node = self.cache[key]  # Find where it is currently parked
            node.value = value  # Overwrite its old data with the new value

            # Move it to the front because it was just updated/used
            self.remove(node)
            self.insert(node)
        else:
            # --- CASE 2: Adding a completely brand new item ---
            new_node = Node(key, value)  # Build a brand new train car
            self.cache[key] = new_node  # Register its key in our fast-pass map
            self.insert(new_node)  # Squeeze it into the front of the line

            # --- CAPACITY CHECK: Did we just exceed our limit? ---
            if len(self.cache) > self.cap:
                # The victim is the absolute oldest car, which always sits right before the Back Gate
                lru_node = self.tail.prev

                # Permanently evict it: erase its map pass and rip it out of the line
                del self.cache[lru_node.key]
                self.remove(lru_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)