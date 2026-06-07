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

