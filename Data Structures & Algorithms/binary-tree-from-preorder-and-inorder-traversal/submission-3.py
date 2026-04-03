# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- First element of preorder is the root of that subtree
- Root of that subtree is in the index seperated left and right subtree in inorder.


Solution:
    1. Use recursive and modifying array
    2. Use recursive DFS with hash map and pointers
"""



class Solution:

    "Use recursive DFS with hash map and pointers"
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # first we need a hashmap to find index in inorder O(1)
        indices = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0 # a pointer always increase after creating a node
        # this one is for node value too 

        # now it is for recursive dfs
        # inside a method so no need for self
        def dfs(l:int, r:int) -> Optional[TreeNode]:
            # now left and right pointer will be like the body guard
            # if we out of bound then it return None
            if l > r:
                return None
            
            # now for creating node and connecting
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)
            # we will find the middle or root node for this current sub tree
            #   base on the value of first preorder which is pre_idx
            #   then find in the hash with val: idx
            mid = indices[root_val]

            # connecting part
            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node

        return dfs(0, (len(inorder) - 1))












    "solution modifying the string with recursive dfs"
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         # use recursive modifying the list base on first and index root of preorder and inorder

#         if not preorder or not inorder: return None

#         # creating the node
#         node = TreeNode(preorder[0])
#         mid = inorder.index(preorder[0])

#         # connecting the node
#         node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#         node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

#         return node

# # Time: O(N^2)
# # Space: O(N)

        