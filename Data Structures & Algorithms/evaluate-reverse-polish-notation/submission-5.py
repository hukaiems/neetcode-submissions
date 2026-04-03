class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        "use stack"
        "push back result after calculation -> always pop 2 elements"
        
        stack = deque()

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-": # reverse order of pop's elements
                a, b = stack.pop(), stack.pop()
                stack.append((b - a))
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a)) # int() can also use for round
            
            else: # not operators -> append
                stack.append(int(i))

        return stack[-1]