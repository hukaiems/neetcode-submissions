import re
import operator

class Solution:

    # in this neetcode doesnt have regex


    def evalRPN(self, tokens: List[str]) -> int:
        """
            Okay, This one will use 1 stack.
            - We need regex to check isit number
            - A hash to check what to do with the string operator
            - If number just append in the stacl
            - if operator then pop out and calculation, remember to put result back in because order is important
            - How can put result back in is correct order ?
            Example: 2 1 - 3 /
            so 2-1 = 1
            put result in now stack will be 1 3
            then 1 / 3 = 0
            or 2 1 2 - + 3 /
            1 -2 = -1, => 2 -1
            2 + -1 = 1 => 1 3 => 1 / 3 = 0

            Actually we can se simple if else for all the operator but use these things help me reuse and like revised
            knowledge, okay let's go.
        """


        """
            The method below doesnt use regex because neetcode doesnt have regex.
        """


        stack = deque()
        for s in tokens:
            # if the s is number just append in the stack
            if s =="+":
                out_2 = stack.pop()
                out_1 = stack.pop()
                result = out_1 + out_2
                stack.append(result)
            elif s =="-":
                out_2 = stack.pop()
                out_1 = stack.pop()
                result = out_1 - out_2
                stack.append(result)
            elif s =="*":
                out_2 = stack.pop()
                out_1 = stack.pop()
                result = out_1 * out_2
                stack.append(result)
            elif s =="/":
                out_2 = stack.pop()
                out_1 = stack.pop()
                result = int(out_1 / out_2) # int in python will subtract near zero
                stack.append(result)
            else:
                stack.append(int(s))

        return int(stack[0])

# Time: O(N)
# Space: O(N)
        
