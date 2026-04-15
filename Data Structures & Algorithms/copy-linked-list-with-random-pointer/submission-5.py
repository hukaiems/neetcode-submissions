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

        # same 2 passes method but use more efficient code
        # create hash with pre initilized None case
        hash_map = {None: None}

        # first pass -> create hash
        cur = head
        while cur:
            copy = Node(cur.val)
            hash_map[cur] = copy
            cur = cur.next
        
        # second pass -> connecting
        cur = head
        while cur:
            copy = hash_map[cur]
            copy.next = hash_map[cur.next] # connecting next ptr using the hashmap
            copy.random = hash_map[cur.random] 
            cur = cur.next
        
        return hash_map[head]


        """
        Using 2 passes
        - First pass to create deep copy and save to the hash_map (create dummy and connect with new copy list)
        - Second pass to connect the random pointer
        """

        # tail = head
        # hash_map = defaultdict(Node)
        # dummy = Node(0)
        # dummy_tail = dummy
        # # first pass
        # while tail:
        #     # we create deep copy and put into hash_map for each node
        #     new_node = Node(tail.val)
        #     hash_map[tail] = new_node
        #     dummy_tail.next = new_node
        #     dummy_tail = dummy_tail.next
        #     tail = tail.next
        
        # # second pass
        # tail = head
        # dummy_tail = dummy.next
        # while tail:
        #     if tail.random is None:
        #         dummy_tail.random is None
        #     else:
        #         dummy_tail.random = hash_map[tail.random]
        #     dummy_tail = dummy_tail.next
        #     tail = tail.next

        # return dummy.next
