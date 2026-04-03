"""
Lesson:
- Managing condition's order so it can explore some path first in backtracking.
- Designing condion carefully and detaily to make it run correctly.
- 2^N is the subset problem, making 2 choices in N times.
- "Generating Parenthesis" is a type of catalan numbers.
"""
"use backtracking + stack"
# stack can help reducing copying time
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # backtrack
        def backtrack(cur: deque(), open_num: int, close_num: int) -> None:
            # base case:
            if len(cur) == n*2:
                res.append("".join(cur))
                return
            
            # 2 choices, open first
            if open_num > 0:
                cur.append('(')
                backtrack(cur, open_num-1, close_num)
                cur.pop()
            # close, only when > open
            if close_num > open_num: # if close 0 then open 0 then it return
                cur.append(')')
                backtrack(cur, open_num, close_num-1)
                cur.pop()
        backtrack(deque(), n, n)
        return res
# Time: O(Cn) only Cn solutions to find, no copying time cause append and pop in stack is O(1)
# Space: O(N) for stack only, recursion is O(2N) == O(N)

# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         """
#         We will use backtracking for this problem.
#         So maybe this is misaligned to put it in Stack =)).

#         Back tracking use recursive function. 
#         Back tracking needs 3 things choice, constraint and goal.
#         Choices to make, constraint to make a new decision and goal to return.
#         Remember to design the constraint so that after an attempt it delete the old trial
#             and can move to the new constraint for a new trial.
#         """

#         stack = deque()
#         res = []

#         def back_tracking(openN, closeN):
#             # check valid string to return
#             if openN == closeN == n:
#                 res.append("".join(stack))
#                 return
            
#             # now constraint so it can make a choice
#             # always have the open parentheses first 
#             if openN < n:
#                 stack.append('(')
#                 # after append we now need to make a choice and to do it we call recursive functio
#                 back_tracking(openN + 1, closeN)
#                 # remember to delete the trial after recursive return for new attempt
#                 stack.pop()

#             # this constraint to add the close one and to create new attempt
#             if closeN < openN:
#                 stack.append(')')
#                 back_tracking(openN, closeN + 1)
#                 stack.pop()

#         back_tracking(0, 0)
#         return res

# # Time: because of catalan around O(4^n / sqrt(n))
# # Space: O(N)