class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Lesson:
        - Can base on monotonic nature to keep track of max or min value
        - Design the order of condition so that some maybe place first but will run last

        Solution:
        - Using monotonic decreasing deque and a sliding window technique
        """

        res = []
        q = deque()

        l, r = 0,0

        for r in range(len(nums)):
            n = nums[r]
            # kick out smaller then append
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(r)

            # kick out left out of bound in q
            if l > q[0]: #this cond run last after l pointer has moved
                q.popleft() 
            
            # if window has formed then append max and move pointer
            if r + 1 >= k: #after form then every step we need to append max
                res.append(nums[q[0]])
                l += 1 # move l pointer after append max
        return res
# Time: O(N)
# Space: O(N)
