# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Handling base case.
- Deque in python process iterable data only.
- BFS iterative need to follow FIFO rule.
- Using return to store the variable for each recursive call.

Solution:
1. Recursive DFS
- 
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        "Recursive DFS"
        if not root: return 0

        # return recursive call 1 + max so that the last caller will have the maximum depth.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))