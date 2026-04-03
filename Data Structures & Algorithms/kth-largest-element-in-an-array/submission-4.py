class Solution:
    "using max heap"
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(nums)
        res = 0

        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        return -res

        
    "using heapq.nlargest library"
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # nlargest will return [arr] of n largest
    #     return heapq.nlargest(k, nums)[-1]