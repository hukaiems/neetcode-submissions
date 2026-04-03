# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Handling base case.
- Deque in python process iterable data only.
- BFS iterative need to follow FIFO rule.
- Using return to store the variable for each recursive call.

Solution:
1. Recursive DFS
    - return 1 + max of 2 side nodes.

2. Iterative BFS
    - Using a deque
        Popping out every node of the level and append children.
        update level after append the children of the next level.

3. Iterative DFS
    - Using a deque stores node and the level of that node.
        Output the max level.

"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        "Iterative DFS"
        # creating the stack
        # append the root with its level in
        # the deque will unpack the iterable so if there is an array we need to put in [[]] when initilize the deque.
        tree_stack = deque([[root, 1]])
        res = 0
        while tree_stack:
            # pop out the node to process
            node, level = tree_stack.popleft()

            # only process exist node.
            if node:
                res = max(res, level)
                tree_stack.append([node.left, 1 + level]) #can append empty node because only exist node will be processed
                tree_stack.append([node.right, 1 + level])
        
        return res




        "Iterative BFS"
        # if not root: return 0

        # # a deque to store node and update level depth
        # tree_queue = deque([root]) # python deque only store iterable
        # level = 0
        # while tree_queue:
        #     # use a for loop to know how many nodes in a level
        #     for i in range(len(tree_queue)):
        #         node = tree_queue.pop()
        #         # check if children exist to append
        #         if node.left:
        #             tree_queue.appendleft(node.left)
        #         if node.right:
        #             tree_queue.appendleft(node.right)

        #     # after handle every node of 1 depth, update that level in.
        #     level +=1

        # return level
# Time: O(N)
# Space: O(k) of the  most nodes in a level.



        "Recursive DFS"
        # if not root: return 0

        # # return recursive call 1 + max so that the last caller will have the maximum depth.
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Time: O(N)
# Space: O(K) for the deepest node store in the recursive stack.