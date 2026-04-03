class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Solution use 2 pointers at both side
        # key:
        # 1. The farther the better
        # 2. The taller the better
        # Summary, if we move on closer then we need to find the higher height to by pass the closure distance.

        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            # find the lower height to calculate the area
            lower_pointer = min(heights[l], heights[r])
            area = lower_pointer * (r - l)

            if( area > max_area):
                max_area = area
            # which side smaller then move it 
            if(heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1

        return max_area

# Time: O(N)
# Space: O(1)