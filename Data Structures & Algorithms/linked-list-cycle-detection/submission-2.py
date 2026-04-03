# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ 
        Lesson:
        - We can save entire a node - object into the hash.
        - Floyd's Tortoise and Hare - Fast and Slow algorithm.

        """


        "1. Hash solution"
        saved_hash = defaultdict(int)
        
        tail = head
        while tail:
            saved_hash[tail] += 1
            if saved_hash[tail] > 1:
                return True # there is 2 same nodes so it is a cycle linked list.
            tail = tail.next # use a while so remember to update the node
        # Linked List pointer reach the None or the end
        return False

# Time: O(N)
# Space: O(N) because of the hash

