class Stack:
    def __init__(self):
        self.items = []

    def push(self, items):
        self.items.append(items)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        is_empty = self.is_empty()
        if is_empty:
            return "IndexError: DynamicArray index out of range"
        return self.items.pop()

    def peek(self):
        is_empty = self.is_empty()
        if is_empty:
            return "IndexError: DynamicArray index out of range"
        return self.items[-1]
