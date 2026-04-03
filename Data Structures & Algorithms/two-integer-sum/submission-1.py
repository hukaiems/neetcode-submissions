from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = defaultdict(int)

        
        for index, value in enumerate(nums):
            diff_num = target - value
            if diff_num in nums_hash:
                return [nums_hash[diff_num], index]
            
            nums_hash[value] = index

        