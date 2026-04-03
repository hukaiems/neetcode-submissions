# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- BFS_Breath First Search can help to reach all the node in the level.
- Always handling the base case first.
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # use the BFS algorithm to reach each level and append the value of the node
        res = []
        # remember to append the root in first
        nodeStack = deque([root])

        while nodeStack:
            temp = []
            # a for loop to capture the level nodes
            for i in range(len(nodeStack)):
                node = nodeStack.pop()
                # if exist then append children
                if node:
                    temp.append(node.val)
                    nodeStack.appendleft(node.left)
                    nodeStack.appendleft(node.right)
            if temp:
                res.append(temp)

        return res