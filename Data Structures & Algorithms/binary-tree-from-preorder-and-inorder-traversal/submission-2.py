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
"""

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # use recursive modifying the list base on first and index root of preorder and inorder

        if not preorder or not inorder: return None

        # creating the node
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # connecting the node
        node.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return node

# Time: O(N^2)
# Space: O(N)

        