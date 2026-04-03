class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlargest will return [arr] of n largest
        return heapq.nlargest(k, nums)[-1]