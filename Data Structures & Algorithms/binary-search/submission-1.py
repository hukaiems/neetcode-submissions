class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search has O(logN) which is log2N = X

        # We use index to process so last index is len() - 1
        start, end = 0, len(nums) - 1

        # why equal? Because sometime start == end and that last element is the target 
        # Whhy is this range?
            # Because if start pass end or vice versa which mean we search whole array and cant find anything match
        while start <= end:
            # This is floor division - chia het lay phan nguyen
            mid = (end + start) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid

        return -1
        
# Time: O(logN)
# Space: O(1)