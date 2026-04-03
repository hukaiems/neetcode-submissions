class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # because only 1 broken cut, 1 without ASC order
        # using mid we can seperate and perform binary on that ASC portion

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid

            # now identifies ASC portion

            # left portion
            if nums[l] <= nums[mid]: # can be equal if same index
                # check if it in the left of the chosen portion
                if nums[l] > target or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # right portion
                if nums[r] < target or target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1 
# Time: O(log(N))
# Space: O(1)