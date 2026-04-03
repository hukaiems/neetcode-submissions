# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Careful with local variable
- With multiple recursive, choose which one to call carefully.
- Modifying the return statement to call the recursive correctly.

Solution:
- Use a check same tree method.
    From that just use recursive isSubtree to check everynode 
        Return only need 1 true so only need to be or for both side.
"""

class Solution:

    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot: return True
        if not root or not subRoot or root.val != subRoot.val: return False

        # if the tree is the same then when it reach the last 2 None nodes it will return True
        # from those True statement it then return True until it reach the top.
        return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check subRoot none
        if not subRoot: return True
        if not root: return False # if sub but not root 

        # check sameTree
        if self.isSameTree(root, subRoot): return True

        # if the current node isnt same tree then check both sides
        # only need 1 subTree to be the same is enough
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))