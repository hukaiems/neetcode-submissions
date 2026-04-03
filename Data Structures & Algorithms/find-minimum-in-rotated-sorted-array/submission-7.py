class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case
        if nums[0] < nums[-1]:
            return nums[0]

        # if it rotated then push inside == find the min
        l, r = 0, len(nums) - 1
        res = nums[r]

        while l <= r:
            mid = (r + l) // 2
            res = min(res, nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return res