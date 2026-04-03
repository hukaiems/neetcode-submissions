# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    "recursive dfs inorder with array"

    # it will append into class var without returning anything
    def dfs(self, root: Optional[TreeNode]) -> None:
        if not root: return

        # go to the  left most with inorder
        # we only need to call the funtion it will append the val in the class var so dont need to store their result.
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        self.dfs(root)

        return self.arr[k-1]

# Time: O(N)
# Space: O(N) for the array