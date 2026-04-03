# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Handling empty node first.
- Recursive return can be discarded.
    Sometimes only need the last caller return.

Solution:
- Preorder inverting 2 nodes before traversing.

"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if the node is empty
        if not root:
            return None
        
        # swap and then recursive to traverse
        l, r = root.left, root.right
        root.left = r
        root.right = l

        # traversing 
        if root.left:
            # pass in the left pointer for the function
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)

        return root
# Time: O(N)
# Space: O(N) because of the recursive stack