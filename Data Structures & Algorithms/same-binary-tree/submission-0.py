# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    # a dfs method for both trees
    def dfsDual(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
        # check if 1 exist but other none
        if p and not q or not p and q:
            self.flag = False
        # now if any of them none then return
        if not p or not q: return

        # go both sides for both trees
        self.dfsDual(p.left, q.left)
        self.dfsDual(p.right, q.right)

        # comparing value
        if p and q and p.val == q.val:
            return
        else:
            self.flag = False
            return

            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # creating a recursive DFS to process both trees at the same time
        # any diff than set flag False

        self.flag = True

        self.dfsDual(p, q)

        return self.flag