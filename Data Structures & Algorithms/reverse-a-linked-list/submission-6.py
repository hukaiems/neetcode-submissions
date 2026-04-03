# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursive
        """

        # base case:
        if not head:
            return None

        # set new_head in case no next node
        new_head = head
        if head.next:
            new_head = self.reverseList(head.next) # this always return the same last node

            # now reverse the current node
            head.next.next = head
        head.next = None # point it to None to prevent cycle

        return new_head
        # Time : O(N) - Space: O(N) recursive callstack



        """
        2 pointers -> iterative
        """

        # prev, cur = None, head
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        
        # return prev
# Time: O(N) - Space: O(1)