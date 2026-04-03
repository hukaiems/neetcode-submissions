# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Lesson:
        - Dummy can help in keeping track of prev node using pointer and create new linked list.
        - DUmmy can be created to connect to head "ListNode(0, head)".
        - Can find the nth node in reversed order with 2 pointers of distance n.


        Solution:
        1. Reverse-Delete-Reverse
        2. Using 2 pointers with distance is n to find the nth node.
            Use dummy to track the prev node with pointer to perform delete.
        """

        # create 2 pointers 
        dummy = ListNode(0, head) # dummy to keep track and prevent error when linked list only 1
        left = dummy
        right = head
        while n > 0 and right:
            right= right.next
            n -= 1
        # now find the prev nth node with 2 pointers has distance n
        while right:
            left = left.next
            right = right.next

        # now find perform delete
        if left and left.next:
            left.next = left.next.next
        else:
            left.next = None

        return dummy.next
        