# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Becareful with the 1 line condition, with mistake it can cause extra running time.

Solution:
1. Recursive Preorder DFS
    - Base on the previous binary tree.
    - We can calculate the max of that subtree and update the class var
    - Then we pick the bigger path and return it for the upper node.
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # creating the sum var.
        self.max_sum = float('-inf')

        # creating the recursive function
        def dfs(root: Optional[TreeNode]) -> int:
            if not root: return 0

            root_val = root.val
            # now we need to  traverse and store max in a value
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            # check if the max is negative then abort that path
            if max_left < 0: max_left = 0
            if max_right < 0: max_right = 0

            total = max_left + root_val + max_right
            self.max_sum = max(self.max_sum, total)

            # lastly return the the root val + max_side
            max_side = max(max_left, max_right)
            return root_val + max_side

        dfs(root)
        return self.max_sum
