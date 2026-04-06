# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Using dummy node technique
        - Dummy node have to set the new head for the linked list
        - Remember to use tail to connect new node into the dummy
        """

        dummy_node = ListNode()
        tail = dummy_node # set the tail

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next # update to the next tail for new connecting

        tail.next = list1 or list2 # if 1 of the list still exist then connect dummy into it

        return dummy_node.next