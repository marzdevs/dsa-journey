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
        self.prev = None  # Pointer to the neighbor on the left
        self.next = None  # Pointer to the neighbor on the right


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()  # The Hash Map for O(1) lookups: maps key -> Node
        self.head = Node(0, 0)  # Permanent boundary gate at the absolute front
        self.tail = Node(0, 0)  # Permanent boundary gate at the absolute back

        # Connect the front and back gates directly to each other at the start
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        # 1. Look at the node's current left and right neighbors
        prev_node = node.prev
        next_node = node.next

        # 2. Tell the neighbors to hold hands with each other, skipping 'node'
        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node: Node):
        # 1. Grab the person currently standing first in line right after the head gate
        current_first = self.head.next

        # 2. The new node reaches out its left hand to hold the head gate
        self.head.next = node
        node.prev = self.head

        # 3. The new node reaches out its right hand to hold the old first person
        node.next = current_first
        current_first.prev = node


    def get(self, key: int) -> int:

        pass

    def put(self, key: int, value: int) -> None:

        pass

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)