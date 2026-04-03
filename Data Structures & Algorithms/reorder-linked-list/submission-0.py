# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Lesson:
        - Fast and slow can also be used to  find middle node.
        - Reverse technique will manipulate the original list.

        Solution:
        - Find middle then reverse the second half and rearrange the head linked list.
        """

        # find the middle using fast and slow pointer
        slow, fast = head, head.next #fast = next will make it reach the end or none in odds which help to stop the loop.
        while fast and fast.next: # fast and fast.next so can secure even list at the last check to make sure None.next wont happen.
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None # after create second pointer then cut the slow.next so can create the complete first half.
        # use 2 pointers to reverse the list
        pre, cur = None, second
        while cur: #run until cur reach None
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # now rearrange the head linked list
        first, second = head, pre
        # use 2 pointers to merge both linked list
        while second: # use secon because when odds second will smaller
            nxt_1 = first.next
            nxt_2 = second.next
            first.next = second
            second.next = nxt_1
            # after connect move pointers
            first = nxt_1
            second = nxt_2

        