class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        """
        This problem is not intuitive, cant figure it out from it own.
        Base on the array, if we use constant memory we have to only traverse it like a pointer use the fast and slow technique.
        The index and the value inside the array will act similarly like a linked list. =))))

        - Tortoise and Hare -> find the first intersect node
        - slow = slow -> find the start of the cycle -> duplicate
        """

        # first pass -> find first intersection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # second pass -> find cycle node
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
# Time: O(N)
# Space: O(1)



        # num_set = set()
        # for n in nums:
        #     if n not in num_set:
        #         num_set.add(n)
        #     else:
        #         return n
# Time: O(N)
# Space: O(N)