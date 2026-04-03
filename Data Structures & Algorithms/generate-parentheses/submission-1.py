class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        We will use backtracking for this problem.
        So maybe this is misaligned to put it in Stack =)).

        Back tracking use recursive function. 
        Back tracking needs 3 things choice, constraint and goal.
        Choices to make, constraint to make a new decision and goal to return.
        Remember to design the constraint so that after an attempt it delete the old trial
            and can move to the new constraint for a new trial.
        """

        stack = deque()
        res = []

        def back_tracking(openN, closeN):
            # check valid string to return
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            # now constraint so it can make a choice
            # always have the open parentheses first 
            if openN < n:
                stack.append('(')
                # after append we now need to make a choice and to do it we call recursive functio
                back_tracking(openN + 1, closeN)
                # remember to delete the trial after recursive return for new attempt
                stack.pop()

            # this constraint to add the close one and to create new attempt
            if closeN < openN:
                stack.append(')')
                back_tracking(openN, closeN + 1)
                stack.pop()

        back_tracking(0, 0)
        return res

# Time: because of catalan around O(4^n / sqrt(n))
# Space: O(N)