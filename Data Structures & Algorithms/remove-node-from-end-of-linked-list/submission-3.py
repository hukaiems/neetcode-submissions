# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        2 passes
            1 for save nodes into a list then remove the nth node
            2 for connect back the list
        """
        # base case
        if not head or not head.next:
            return None

        tail = head
        arr = []
        while tail:
            nxt = tail.next
            tail.next = None
            arr.append(tail)
            tail = nxt
        
        arr.pop(-n) # pop out 

        tail = arr[0]
        for i in range(1, len(arr)):
            tail.next = arr[i]
            tail = tail.next
        
        return arr[0]