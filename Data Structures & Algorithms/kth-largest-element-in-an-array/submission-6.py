"""
Lesson:
- Remember to put return before calling recursion to get back the result

Solution:
    1. Max heap
    2. Quick select (base on quick sort)
        - choose the last idx at pivot
        - Swap p to i if i < pivot
        - last swap then call recursion until find it.
"""

class Solution:

    "using quick select"
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # because we find the Nlargest so we need to set
        k = len(nums) - k

        def quick_select(l: int, r: int) -> int:
            # initilize pivot and p pointer
            pivot, p = nums[r], l
            # for loop to do the swap and place pivot
            for i in range(l, r): # stop before last element which is pivot so p wont go out of idx and cause infinite loop
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # last swap
            nums[p], nums[r] = nums[r], nums[p]
            
            # now begin checking
            if p > k:
                return quick_select(l, p-1)
            elif p <k:
                return quick_select(p+1, r)
            else:
                return nums[p]
        return quick_select(0, len(nums)- 1)
# Time: O(N) or worst O(N^2)
# Space: O(1)



    "using max heap"
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     for i in range(len(nums)):
    #         nums[i] = -nums[i]
        
    #     heapq.heapify(nums)
    #     res = 0

    #     while k > 0:
    #         res = heapq.heappop(nums)
    #         k -= 1
    #     return -res
# Time: O( N + k logN)
# Space: O(N)

        
    "using heapq.nlargest library"
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # nlargest will return [arr] of n largest
    #     return heapq.nlargest(k, nums)[-1]