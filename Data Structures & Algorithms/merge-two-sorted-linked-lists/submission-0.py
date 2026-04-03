# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Lesson:
        - Use dummy node technique
            Create a new node to keep connect and create new linked list
        """

        # create the dummny node
        dummy = ListNode()
        tail = dummy # a tail pointer will help us to connect and create new link

        # loop until 1 of the head is None to connect all of them
        while list1 and list2:
            if list1.val < list2.val: # if smaller then connect to the tail pointer
                tail.next = list1
                # update the pointer of the list1 because we just connect the current pointer already
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #updating the tail pointer to the new node
        # there is one more case when one head is None we then need to connect the other left
        #    Head into the dummy linked list
        if not list1:
            tail.next = list2
        else:
            tail.next = list1
        # now remove dummy head and use the real smallest node
        return dummy.next

# Time: O(N + M) because of 2 linked list lengths
# Space: O(1)