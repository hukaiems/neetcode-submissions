# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Read the description and constraint carefully to come up the most optimal solution.
- LCA in a binary search tree is a node lies between p and q node.

Solution:
- Using a while loop.
    If cur between p and q the it is the LCA.
    If not then move to the suitable sides.
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # a pointer to loop through the binary search tree

        cur = root
        # a while loop
        while cur: #the constraint said it will exist the LCA node.
            # if both p and q is bigger or smaller move to the appropriate sides.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                # we have found it. LCA is node lies between p and q node.
                return cur

# Time: O(max depth of logN)
# Space: O(1)