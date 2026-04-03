class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort -> choose first val -> 2pointers other
        # remember to skip duplicate
        # for loop will also skip duplicate

        nums = sorted(nums)
        res = []

        for i, first in enumerate(nums):
            # if first val > 0 -> No triplet exist
            if first > 0: break

            # check duplicate
            if i > 0 and first == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                second = nums[l]
                third = nums[r]
                total = first + second + third

                if total == 0:
                    res.append([first, second, third])
                    l += 1
                    r -= 1
                    # skip duplicate after found
                    while nums[l] == second and l< r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
            
        
        return res