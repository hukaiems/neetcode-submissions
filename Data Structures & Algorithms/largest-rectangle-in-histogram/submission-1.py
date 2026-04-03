class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        A monotonic increasing stack problem
            - If the current height is shorter then pop out higher height.
                Why? Because the higher height cant expand anymore to the left
            - Remember to calculate are for each popped height.
            - Save the index of the last popped height for the current height.
                Why? Because shorter height can expand to the higher previous one.


        Try to think about monotonic increasing or decreasing
            Those are really suitable for stack problem.
        """

        stack = deque()
        max_area = 0

        for i, h in enumerate(heights):
            # if higher then pop out
            #   Because it cant expand anymore
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start = index

            # if nothing in stack or higer height append it
            stack.append((start, h))
        
        # now after loop through the heights
        #  We loop through the stack to calculate left over height
        #    These are the one who can expand until the end.
        for i, h in stack:
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area

# Time: O(N)
# Space: O(N)
    