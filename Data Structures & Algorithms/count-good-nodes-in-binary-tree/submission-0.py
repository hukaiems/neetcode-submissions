# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Think about what does the recursive will give back from that to easier manipulate variable.
"""

class Solution:


    # creating the recursive preorder comparision dfs method
    def recursiveDfsMax(self, root: TreeNode, max_val: int) -> int:
        # so it will give back the result or the good nodes it found
        if not root: return 0

        res = 1 if root.val >= max_val else 0
        max_val = max(max_val, root.val)
        # now we will traverse through both sides
        # and each traverse will give us back the res of that subtrees
        # we then use the res variable to plus with the return back var
        res += self.recursiveDfsMax(root.left, max_val)
        res += self.recursiveDfsMax(root.right, max_val)

        return res

    def goodNodes(self, root: TreeNode) -> int:
        # we will use recursive Dfs

        return self.recursiveDfsMax(root, root.val)

# Time: O(N)
# Space: O(H)