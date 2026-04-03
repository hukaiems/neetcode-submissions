# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Infinity -> "inf"
- Think about the range of  the answer or condition to create solution.
"""

class Solution:
    def dfsRange(self, root: Optional[TreeNode], left=float('-inf'), right=float('inf')) -> bool:
        if not root: return True

        # check the condition
        if (left < root.val < right):
            return self.dfsRange(root.left, left, root.val) and self.dfsRange(root.right, root.val, right)
        else:
            return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # use dfs method and pass down the range for comparision

        return self.dfsRange(root)

# Time: O(N)
# Space: O(H)

