# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Most of the BS problems can solve by BFS or DFS.
- Starting from the BFS or DFS to build the algorithm.
"""

class Solution:
    # creating a dfs method for comparing the height
    def recursiveDfs(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # recursive call for both subtree
        left_height = self.recursiveDfs(root.left)
        right_height = self.recursiveDfs(root.right)

        # comparison
        if abs(left_height - right_height) > 1:
            self.flag = False
        
        # return the height of each node
        return 1 + max(left_height, right_height)  #only take the deepest height in each side

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # set a flag and call recursive if diff heght > 1 flag false

        self.flag = True

        self.recursiveDfs(root)

        return self.flag

# Time: O(N)
# Space: O(max depth)