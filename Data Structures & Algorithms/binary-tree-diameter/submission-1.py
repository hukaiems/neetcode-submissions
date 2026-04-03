# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Recursive DFS Binary tree can work with global variable.
- An inner function needs self. var to change outside var.
- Recursive can call itself directly inside it.
"""

class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        "Recursive with global var"

        self.res = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if not root: return 0 # those NOne node will be return 0 immediately so wont get wrong depth cause last return line 
            # doesnt reach

            left = dfs(root.left)
            right = dfs(root.right)

            # after both sides return plus both of the path
            self.res = max(self.res, left + right) # because the longest path is both sides plus each other
            return 1 + max(left, right) # can only choose 1 path to move to upper node.

        # call the function 
        dfs(root)
        return self.res # because it is a class variable

# Time: O(N)
# Space: O(max depth)