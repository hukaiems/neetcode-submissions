class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = dict()

        idx = 0
        for idx in range(len(nums)):
            res = target - nums[idx]
            if res in hashMap:
                return [hashMap[res], idx]
            
            hashMap[nums[idx]] = idx
            idx += 1
# Time: O(N)
# Space: O(N)


        # old way not optimize enough to solve all the test case
        # idx_hash = dict()

        # i = 0
        # # assign index to value into the dict
        # for i in range(len(nums)):
        #     idx_hash[nums[i]] = i
        
        # l, r = 0, len(nums) - 1
        # sorted_nums = sorted(nums)

        # while l < r:
        #     total = sorted_nums[l] + sorted_nums[r]
        #     if total == target:
        #         idx_l = idx_hash[sorted_nums[l]]
        #         idx_r = idx_hash[sorted_nums[r]]
        #         if idx_l > idx_r:
        #             return [idx_r, idx_l]
        #         else:
        #             return [idx_l, idx_r]
            
        #     elif total > target:
        #         r -= 1
        #     else:
        #         l += 1
