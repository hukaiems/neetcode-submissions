# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # using  BFS and take only last node for the res

        res = []

        if not root: return res

        nodeQueue = deque([root]) # remember to add the root in first =)))
        while nodeQueue:
            flag = True
            # okay start for loop for each level
            for i in range(len(nodeQueue)):
                # if this is the beginning of the level loop
                if flag:
                    node = nodeQueue[0]
                    res.append(node.val)
                    flag = False
                
                # now traverse everynode to reach the lower level
                node = nodeQueue.pop()
                # cant append None because we need to take the last node.
                if node.left:
                    nodeQueue.appendleft(node.left)
                if node.right:
                    nodeQueue.appendleft(node.right)
            
        return res