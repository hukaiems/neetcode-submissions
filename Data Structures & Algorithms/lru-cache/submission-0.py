"""
Lesson:
- Doubly linked list can help using only 1 node to control the whole list
- Linked list can use to keep track of time usage like LRU.

Solution:
- We need a hash so get() method can find in O(1).
- We need a doubly linked list so put() method can run in O(1).
- We need 2 pointers or 2 dummy nodes at the side to keep track of the LRU and MRU and maintaining the node.
"""

# creating the ListNode
class ListNode: #it will store key value, prev, next. key is for accessing the node with key inside it without knowing the key.
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    # we need 2 helper functions insert and remove the node in the linked list to help running in O(1) time.
    def remove(self, node)-> None:
        # to delete a node we need to connect prev and next node to each other
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


    def insert(self, node) -> None:
        # only insert next to the left of the right pointer for MRU position
        prev_node, next_node = self.right.prev, self.right
        # connect pointers to the node
        prev_node.next = node
        next_node.prev = node
        # connect node to pointers
        node.prev = prev_node
        node.next = next_node


    def __init__(self, capacity: int):
        # we need 2 pointers for the linked list, capacity of cache and a hash
        self.capacity = capacity
        self.hashCache = {}
        self.left, self.right = ListNode(), ListNode()
        # connecting 2 pointers to create the Linked List
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        # find in the hashCache and return
        if key in self.hashCache:
            # delete the node position to update
            self.remove(self.hashCache[key])
            self.insert(self.hashCache[key])
            return self.right.prev.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        newNode = ListNode(key, value)
        # check is the key exist yet 
        if key in self.hashCache:
            # delete the current node position
            self.remove(self.hashCache[key])
        # then updating the new value in hash and then in linked list
        self.hashCache[key] = newNode
        self.insert(self.hashCache[key])

        # check if the cache is limit
        if len(self.hashCache) > self.capacity:
            # delete the lru position
            lru = self.left.next
            # delete in linked list and in hashCache
            self.remove(lru)
            del self.hashCache[lru.key] #if we dont store key and we got a node we need to loop through hash to find correct node to del


        
