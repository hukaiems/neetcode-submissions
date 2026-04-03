class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first pass for before product
        num = 1
        res = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                res[i] = num
                continue
            num*= nums[i-1]
            res[i] = num

        print(res)

        num = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                res[i] *= num
                continue
            num *= nums[i+1]
            res[i] *= num

        return res

# TIme: O(N)
# Space: O(1) without answered list
