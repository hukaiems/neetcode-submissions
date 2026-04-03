# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        "Optimal Recursive Preorder DFS"
        # check 2 of them is None
        if not p and not q: return True

        # check value or if any of them none then False
        if not p or not q or p.val != q.val: return False

        # return True only when both sides is true, meaning both sides is the same
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

    "work but a little bit long syntax"
#     # a dfs method for both trees
#     def dfsDual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
#         # check if 1 exist but other none
#         if p and not q or not p and q:
#             self.flag = False
#         # now if any of them none then return
#         if not p or not q: return

#         # go both sides for both trees
#         self.dfsDual(p.left, q.left)
#         self.dfsDual(p.right, q.right)

#         # comparing value
#         if p.val == q.val:
#             return
#         else:
#             self.flag = False
#             return

            

#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         # creating a recursive DFS to process both trees at the same time
#         # any diff than set flag False

#         self.flag = True

#         self.dfsDual(p, q)

#         return self.flag

# # Time: O(N)
# # Space: O(max depth)