# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
lesson:
- Based on the reversed linked list problem to help solving this.
- Dummy node can help to keep track of the linked list if we change the head pointer.
- Snake_case for var, Camel cases for Classes.

Solution:
- Using 2 pointers to find the k list.
     then send it to the method function to reverse it 
     after that connect it to the dummy 
     continue until the end.
"""


class Solution:
    # creating the reversing linked list method
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use 2 pointers to reverse it
        prev, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # use 2 pointers to traverse and create a dummy node
        dummy = ListNode()
        tail_dummy = dummy

        tail = cur_head = head
        count = 0
        # now a while loop to loop through the linked list
        while tail:
            count += 1
            # check if the count == k
            if count == k:
                # reseting the count var
                count = 0
                # we then cut the tail, save next node then send it to method
                next_node = tail.next
                tail.next = None
                new_head = self.reverseList(cur_head)

                # after return use it to connect to dummy
                tail_dummy.next = new_head
                # updating tail_dummy and 2 pointers
                tail_dummy = cur_head #because after reversed cur_head is the last node
                tail = cur_head = next_node
            
            else:
                tail = tail.next
        # we need a last check because if the left nodes < k then we need to connect it to the dummy
        if cur_head:
            tail_dummy.next = cur_head

        return dummy.next
