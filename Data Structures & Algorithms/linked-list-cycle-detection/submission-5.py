# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Tortoise and Hare optimal
        """

        slow, fast = head, head # slow and fast always catch up cause fast go twice the speed at slow
        
        while fast and fast.next: # we move fast farther so we choose fast
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # use node to compare
                return True 
        
        return False