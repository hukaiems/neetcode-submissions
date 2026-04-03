# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Solution:
- Using merge sort to reduce the merging part of each linked list
    Creating a merge lists method for helping merge part.
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check if the list is None
        if not lists:
            return None
        
        # begin to merge sort linked lists
        while len(lists) > 1:
            # creating an array for keeping new merged lists
            mergedLists = []
            
            # a loop to cut in half
            for i in range(0, len(lists), 2): #merge each pair 
                l1 = lists[i]
                # l2 can be None due to odds
                l2 = lists[i + 1] if i+1 < len(lists) else None
                # append the new merged list
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists # updating the new lists for "lists" var
        
        return lists[0]

        

    # creating merge method
    def mergeLists(self, l1: ListNode, l2: ListNode) ->ListNode:
        # a dummy node to connect 2 linked lists into a new linked list
        dummy = ListNode()
        tail = dummy 

        # the loop run until both lists are empty
        while l1 or l2:
            # create a check if any of them are None
            l1_val = l1.val if l1 else float("infinity")
            l2_val = l2.val if l2 else float("infinity")
            if l1_val < l2_val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # move tail to the new node
            tail = tail.next

        return dummy.next