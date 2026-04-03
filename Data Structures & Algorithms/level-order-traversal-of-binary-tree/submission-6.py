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


Solution: 
1. If append the None Node and have condition to check if it is none to append val and child needs an if temp
2. If dont append None node then have to create a base case condition.
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # use the BFS algorithm to reach each level and append the value of the node
        res = []
        if not root: return res
        # remember to append the root in first
        nodeStack = deque([root])


        while nodeStack:
            temp = []

            for i in range(len(nodeStack)):
                node = nodeStack.pop()

                temp.append(node.val)
                if node.left:
                    nodeStack.appendleft(node.left)
                if node.right:
                    nodeStack.appendleft(node.right)
            res.append(temp)

        return res



        # while nodeStack:
        #     temp = []
        #     # a for loop to capture the level nodes
        #     for i in range(len(nodeStack)):
        #         node = nodeStack.pop()
        #         # if exist then append children
        #         if node:
        #             temp.append(node.val)
        #             nodeStack.appendleft(node.left)
        #             nodeStack.appendleft(node.right)
        #     if temp:
        #         res.append(temp)

        # return res

# Time: O(N)
# Space: O(N)