# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Lesson:
        - Single line if else code can help to create many cases in 1 loop and clean code.
        - a While loop with many or condition can help to get over many edge cases.
        - Paying attention to use operator for creating variable base on math.


        Solution:
        - Creating 2 pointers for 2 linked lists
        - Using a dummy node to connecting and creating the new linked list.
        - Each pass will create sum value of the 2 val in linked lists and the carry value.
        """

        # pointers and dummy node and carry var
        first, second = l1, l2
        dummy = ListNode()
        dummy_tail = dummy
        carry = 0

        # a loop to pass and creating new linked list
        while first or second or carry == 1:  #if any of these still exist the pass continue and a new node borned
            val_1 = first.val if first else 0
            val_2 = second.val if second else 0    #check if it exist
            new_val = val_1 + val_2 + carry

            # caluclating carry and creating new node
            carry = new_val // 10
            new_val = new_val % 10   #take the left out
            newNode = ListNode(new_val)

            # connecting and moving on
            dummy_tail.next = newNode
            dummy_tail = dummy_tail.next
            first = first.next if first else None
            second = second.next if second else None # check if linked list still exist

        return dummy.next
