# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Implement using recursive

        Key:
        - Recursive is tricky in modify pointer
            Visualize it, the more I do the more familiar it will be.
        """

        # [1]->[2]->[3]
        # check if linkedList exits
        if not head:
            return None

        # begin to reverse
        # the newHead will be the current firstr
        # also for the last node because last node doesnt have head.next
        # so it needs a base var which is newHead = head so it can return
        newHead = head
        # but if there is next pointer then newHead equal that next
        if head.next:
            newHead = self.reverseList(head.next)
            # now perform link the current head to the new linked list
            # which mean link the next pointer of the old list 
            # [1]->[2]<-[3], now link [2]-><-[1]
            head.next.next = head

        head.next = None

        return newHead















        "Implement the 2 pointers solution"

        """
        Key:
        - Save the next node so we can access it later on
        - Take advantage of the last node has next pointer point to None
            to stop the loop
        """
        # if not head: #check if the Linked List is empty
        #     return None

        # prev , cur = None, head
        
        # # now if cur node exist save the next node and make it point to prev node
        # # a loop to iterate through linked list using cur exist and cur = nxt pointer
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = nxt
        # # at the last iteration the cur = None then the only prev
        # # now prev is the head
        # return prev






        