class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0

        new_nums = set()

        for i in range(len(nums)):
            if nums[i] not in new_nums:
                new_nums.add(nums[i])
        
        if len(new_nums) < len(nums):
            return True
        return False
            