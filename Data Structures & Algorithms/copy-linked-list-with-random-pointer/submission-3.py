"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
        Using 2 passes
        - First pass to create deep copy and save to the hash_map (create dummy and connect with new copy list)
        - Second pass to connect the random pointer
        """

        tail = head
        hash_map = defaultdict(Node)
        dummy = Node(0)
        dummy_tail = dummy
        # first pass
        while tail:
            # we create deep copy and put into hash_map for each node
            new_node = Node(tail.val)
            hash_map[tail] = new_node
            dummy_tail.next = new_node
            dummy_tail = dummy_tail.next
            tail = tail.next
        
        # second pass
        tail = head
        dummy_tail = dummy.next
        while tail:
            if tail.random is None:
                dummy_tail.random is None
            else:
                dummy_tail.random = hash_map[tail.random]
            dummy_tail = dummy_tail.next
            tail = tail.next
            
        return dummy.next
