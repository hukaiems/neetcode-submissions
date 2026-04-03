class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using a array contains 2 values value and index then sort it and using 2 pointer

        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))

        # sort
        sorted_nums = sorted(arr)

        # use 2 pointers
        l, r = 0, len(nums) - 1
        while l <= r:
            result = sorted_nums[l][0] + sorted_nums[r][0]
            if (result == target):
                return sorted([sorted_nums[l][1], sorted_nums[r][1]])
        
        # no need for other case cause there is always a result
            if result > target:
                r -= 1
            else:
                l += 1