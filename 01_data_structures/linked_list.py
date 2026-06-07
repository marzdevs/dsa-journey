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