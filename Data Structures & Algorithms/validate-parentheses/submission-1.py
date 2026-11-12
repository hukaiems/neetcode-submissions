from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c in ("(", "[", "{"):
                stack.append(c)
            else:
                if not stack:
                    return False
                
                pushed_c = stack.pop()
                if c == ")" and pushed_c != "(":
                    return False
                elif c == "]" and pushed_c != "[":
                    return False
                elif c == "}" and pushed_c != "{":
                    return False
        return len(stack) == 0