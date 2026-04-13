# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1 pass
            Use 2 pointers + dummy node
            set distance between 2 pointers == n
            use dummy to move the left pointer forward 1 node so it can reach right before the delete node
            when the right node reach Null than we can begin to delete node
        """

        # create dummy
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, dummy.next # always have >=1 node

        # set right ptr
        distance = 0
        while right and distance != n:
            right = right.next
            distance += 1

        # move right to reach None
        while right:
            left = left.next
            right = right.next
        
        # delete node -> left now next to the delete node
        left.next = left.next.next

        return dummy.next
# Time: O(N)
# Space: O(1)


        """
        2 passes
            1 for save nodes into a list then remove the nth node
            2 for connect back the list
        """
        # base case
        # if not head or not head.next:
        #     return None

        # tail = head
        # arr = []
        # while tail:
        #     nxt = tail.next
        #     tail.next = None
        #     arr.append(tail)
        #     tail = nxt
        
        # arr.pop(-n) # pop out 

        # tail = arr[0]
        # for i in range(1, len(arr)):
        #     tail.next = arr[i]
        #     tail = tail.next
        
        # return arr[0]
# Time: O(N)
# Space: O(N)