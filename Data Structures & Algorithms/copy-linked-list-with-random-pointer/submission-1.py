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
        Lesson:
        - Initilizing the base case in data structure -> {None: None}
        - 1 pass can do many actions.
        - Defaultdict helps to read unexisted key in the hash.

        Solution:
        - Using 2 passes
            1 for creating the hash with new node
            1 for connecting the new node base on the old linked list.
        """

        # creating the hash

        new_hash = {None: None}     #handle the base case when random pointer point to Null
        tail = head
        while tail:
            copy = Node(tail.val)   # creating new node
            new_hash[tail] = copy
            tail = tail.next
        
        # connecting the new node
        tail = head
        while tail:
            copy = new_hash[tail]   #take out the copy
            copy.next = new_hash[tail.next]
            copy.random = new_hash[tail.random]
            tail = tail.next
        
        return new_hash[head] # can access the new head with key of old node in hash map

# Time: 

