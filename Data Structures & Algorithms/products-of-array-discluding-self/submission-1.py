class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)
        # need 2 passes, 1 for prefix and 1 for post fix
        # the product of both passes will be stored into anwer array
        # prefix first
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

        # now the second pass for postfix
        # the second pass will be reversed from the bottem
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer