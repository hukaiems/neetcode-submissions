class MinStack:
    """
    Using 2 stack for this problem
    1 for storing like normal stack
    1 for tracking which is the minimum value in the original stack right now 
    How to track?
    - simply append the first value if the tracking stack is empty
    - Now if any value equal or smaller then append to the tracking stack
    - we will got a list of tracking min value
    - Remember to pop it out if the pop value in origin is match with the latest [-1] in tracking stack
    """

    def __init__(self):
        # 2 stack 1 original, 1 tracking
        self.stack = deque()
        self.stack_tracking = deque()

    def push(self, val: int) -> None:
        # if trackinng empty push it in cause every element will be the minimum
        # and if the last tracking element is bigger than value then append value in
        self.stack.append(val)
        if not self.stack_tracking or self.stack_tracking[-1] >= val:
            self.stack_tracking.append(val)

    def pop(self) -> None:
        # if the pop element in origin equal to last tracking element, pop all stack
        out = self.stack.pop()
        if out == self.stack_tracking[-1]:
            self.stack_tracking.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.stack_tracking:
            return self.stack_tracking[-1]
        else:
            return None
        
