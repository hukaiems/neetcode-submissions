class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use 2 pointers and move the smaller line
        # the closer the line the smaller it get so we move the shorter one to find the higher line
        # and from that by pass the shortage in width aspect

        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            left_h = heights[l]
            right_h = heights[r]
            distance = r - l

            if left_h < right_h:
                total = left_h * distance
                l += 1
            else:
                total = right_h * distance
                r -= 1
            
            res = max(total, res)
        
        return res
# Time: O(N)
# Space: O(1)