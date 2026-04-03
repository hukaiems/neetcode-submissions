class Solution:
    def isValid(self, s: str) -> bool:
        # use stack due to stack use LIFO
        # and the brackets close follows LIFO
        
        stack = deque()
        for b in s:
            if b == "(":
                stack.append(")")
            elif b == "[":
                stack.append("]")
            elif b == "{":
                stack.append("}")
            else:
                # now we compare using stack
                if stack and b == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        if not stack: # stack empty -> correct
            return True
        
        return False
