"""
My ownn method using 2 stack
1 for storing, 1 tracking the minimum, by adding the smaller or equal value into the stack
- only pop out the minimum_stack if the stack's pop == min's pop
"""

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minimum = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum:
            self.minimum.append(val)
        elif self.minimum[-1] >= val: # only append when >=
            self.minimum.append(val)

    def pop(self) -> None:
        if self.stack and self.minimum and self.stack[-1] == self.minimum[-1]:
            self.stack.pop()
            self.minimum.pop()
        elif self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
