class Solution:
    def isValid(self, s: str) -> bool:
        # use the advantage of the stack FiLO 
        # use the hash map we have learnt to know which open bracket belong to which close bracket

        # this just a list in python
        stack = []

        close_hash = {')': '(', ']': '[', '}': '{'}

        for c in s:
            # if it is a close bracket:
            if c in close_hash:
                if stack and stack[-1] == close_hash[c]:
                    stack.pop()
                # if stack contain open bracket doesnt exist then return false 
                # or the opening and closing bracket are different
                else:
                    return False
            # if it is an open one then just append all
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
