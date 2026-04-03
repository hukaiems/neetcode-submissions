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

        "2. Tortoise and Hare algorithm solution - Fast and slow pointer"
        slow, fast = head, head
        # while loop condition need to check fast.next too because if the linked list isnt a cycle one
        # it can cause the None.next which will raise error.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # the Tortoise has been catched by the Hare return.
                return True
        
        # it isnt a cycle linked list because it has exist the loop so return
        return False

# Time: O(N) it will catch in linear time because distance -= 1 in every step and the farthest distance is equal N.
# Space: O(1) because we only use pointers.

        "1. Hash solution"
#         saved_hash = defaultdict(int)
        
#         tail = head
#         while tail:
#             saved_hash[tail] += 1
#             if saved_hash[tail] > 1:
#                 return True # there is 2 same nodes so it is a cycle linked list.
#             tail = tail.next # use a while so remember to update the node
#         # Linked List pointer reach the None or the end
#         return False

# # Time: O(N)
# # Space: O(N) because of the hash

