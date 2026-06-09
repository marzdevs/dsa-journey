class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0  # Changed to _size to avoid naming conflicts

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1
        return new_node

    def pop_front(self):
        if self.empty():
            raise IndexError('empty list')
        popped_value = self.head.val
        self.head = self.head.next
        self._size -= 1
        return popped_value

    def push_back(self, value):
        # Create the new node container
        new_node = Node(value)

        # Case 1: If the list is completely empty
        if self.empty():
            self.head = new_node

        # Case 2: The list already has items
        else:
            current = self.head
            # Loop until 'current' is sitting on the very last node
            while current.next is not None:
                current = current.next
            # Link the last node's train hitch to our new node
            current.next = new_node

            # Don't forget to increase the size!
        self._size += 1

    def pop_back(self):
        # 1. Check if the train is completely empty
        if self.empty():
            raise IndexError('empty list')

        # 2. Scenario A: Only 1 item in the list (The engine is the caboose)
        if self.head.next is None:
            popped_value = self.head.val
            self.head = None
            self._size -= 1
            return popped_value

        # 3. Scenario B: Multiple items in the list
        current = self.head  # Start our guide at the front engine

        # Walk down the track until current is standing on the second-to-last node
        while current.next.next is not None:
            current = current.next

        # Grab the cargo value from the last node (caboose)
        popped_value = current.next.val

        # Unhook the last node by making current the new end of the train
        current.next = None

        # Shrink the size tracker and return the cargo
        self._size -= 1
        return popped_value