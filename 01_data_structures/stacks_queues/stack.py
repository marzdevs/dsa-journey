class Stack:
    def __init__(self, max_size= None):
        self.items = []
        # Store the maximum capacity limit
        self.max_size = max_size

    def is_full(self):
        # The stack is full if its current size equals the max size
        return len(self.items) == self.max_size

    def push(self, items):
        if self.is_full():
            return "StackOverflowError: Stack is full"
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

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    print("--- Starting Stack Tests ---")
    my_stack = Stack()

    # 1. Test Initial State
    print("Is empty initially?:", my_stack.is_empty())  # Expected: True
    print("Initial size:", my_stack.size())  # Expected: 0
    print("Peek empty stack:", my_stack.peek())  # Expected: IndexError: DynamicArray index out of range
    print("Pop empty stack:", my_stack.pop())  # Expected: IndexError: DynamicArray index out of range
    print("-" * 30)

    # 2. Test Pushing Items (LIFO order)
    print("Pushing: 10, 20, 30")
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("Is empty now?:", my_stack.is_empty())  # Expected: False
    print("Current size:", my_stack.size())  # Expected: 3
    print("Peek top item (should be 30):", my_stack.peek())  # Expected: 30
    print("-" * 30)

    # 3. Test Popping Items
    print("Popped item (should be 30):", my_stack.pop())  # Expected: 30
    print("Peek top item after pop (should be 20):", my_stack.peek())  # Expected: 20
    print("Current size:", my_stack.size())  # Expected: 2
    print("-" * 30)

    # 4. Test Clearing out the Stack
    print("Popped item:", my_stack.pop())  # Expected: 20
    print("Popped item:", my_stack.pop())  # Expected: 10
    print("Size after clearing:", my_stack.size())  # Expected: 0
    print("Is empty after clearing?:", my_stack.is_empty())  # Expected: True
    print("Pop from cleared stack:", my_stack.pop())  # Expected: IndexError: DynamicArray index out of range
    print("--- All Tests Completed ---")