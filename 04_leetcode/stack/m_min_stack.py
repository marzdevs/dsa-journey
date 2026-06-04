"""
Problem: Min stSTack
URL: 
Difficulty: [Easy / Medium / Hard]
Pattern: 

Time Complexity: O()
Space Complexity: O()
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # If MinStack is empty, use 'val'. Otherwise, pick the smaller of the two.
        new_min = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()