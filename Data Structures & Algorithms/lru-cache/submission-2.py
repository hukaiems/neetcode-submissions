"""
Problem Requirements: Both `get()` and `put()` must run in strictly O(1) time.

- Hash Map: Provides the O(1) lookup speed needed for `get()`.
- The Challenge: Tracking the Least Recently Used (LRU) item usually takes O(N) time.
    - Solution: Pair the Hash Map with a Doubly Linked List (DLL).
    - How it works: The Hash Map values store direct pointers to the DLL nodes.
    - Why it works: This entirely eliminates the O(N) search time of a standard linked list. 
    - The Result: We get O(1) direct access via the Map, combined with O(1) node removal and insertion 
        via the Doubly Linked List to instantly update our LRU/MRU order.
"""
class Node:
    def __init__(self, key, value):# it need 2 connect ptrs
        self.value = value
        self.key = key
        self. prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int): # needs hash + DLL
        self.cache = defaultdict() # hash map -> O(1) for get
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0) # LRU and MRU
        self.left.next, self.right.prev = self.right, self.left # connect 2 LRU and MRU -> DLL
    
    def insert(self, new_node):
        # insert to MRU position
        left_node = self.right.prev
        left_node.next = new_node
        new_node.prev = left_node
        new_node.next = self.right
        self.right.prev = new_node
    
    def remove(self, delete_node):
        left_node, right_node = delete_node.prev, delete_node.next
        left_node.next, right_node.prev = right_node, left_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # update LRU DLL
            self.remove(self.cache[key]) # remove out of the DLL
            self.insert(self.cache[key]) # add back to the MRU position
            return self.cache[key].value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # check dup
        if key in self.cache:
            self.remove(self.cache[key]) # delete the dup node
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key]) # add the new node into the list

        # check capacity
        if len(self.cache) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
        
