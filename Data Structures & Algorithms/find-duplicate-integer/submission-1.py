class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Lesson:
        - Floyd's is for finding cycle.
            2 pointers meet at s = 2slow = fast
        - The distance from start to the begining will always equal intersect to begining cycle.
            Although the intersect to begining point can run through many laps in the cycle.
        """

        # Phase 1: fast and flow intersect node
        slow = fast = 0
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Phase 2: find the begining of the cycle or the repeated number
        slow_2 = 0
        while True:
            slow = nums[slow]   
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow

# Time: O(N)
# Space: O(1)