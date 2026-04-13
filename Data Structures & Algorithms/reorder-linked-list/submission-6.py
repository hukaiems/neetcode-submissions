# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursiveReverse(self, head: Optional[ListNode]) -> ListNode:
        # no need for base case

        # point to it self first
        new_head = head
        while head.next: # check for next node -> find the last node to perform recursive reverse
            new_head = self.recursiveReverse(head.next)

            # now when it return back the reverse list, point the current head to itself
            head.next.next = head
            head.next = None
        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Find the middle node, cut it, reverse the second list and merge them
        """
        # base case
        if not head:
            return None
        elif not head.next:
            return

        # First find the middle node using Tortoise and hare
        # put the fast 1 step ahead so it will reach the end faster -> slow will reach mid node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now slow = mid node, cut it
        mid_node = slow.next
        slow.next = None

        # reverse the second list using recursive
        second_head = self.recursiveReverse(mid_node)

        # now merge =)))
        first, second = head, second_head
        while first and second:
            first_next = first.next
            first.next = second
            second_next = second.next
            second.next = first_next
            first = first_next
            second = second_next

# Time: O(N)
# Space: O(N) -> recursive
        


        
