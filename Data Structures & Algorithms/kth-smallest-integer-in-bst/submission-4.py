# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
- Append string in python is copying string which cause O(N^2)
- Recursive function can return nothing.
- 

Solution:
1. Recursive inorder dfs with array
    Follow inorder recursive and append val into class array.

2. Iterative inorder DFS with stack - quite interesting combination of iterative and stack isnt it? =))))
    Store tree node in a stack
    Call recursive follows inorder method
    then pop out the node in the stack to reverse.

    Explaination:
        We can say it has 2 stages:
        1. Keep append in the stack and go to the left
        2. Keep popping and go to the right
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        "iterative dfs with stack and inorder"
        # we will try
        n = 0
        tree_stack = deque()
        # we need a pointer for iterative loop
        cur = root

        # now for the iterative loop
        while cur or tree_stack: # only need 1 to run
            # now we need to go to the left most or follow inorder
            while cur:
                tree_stack.append(cur)
                cur = cur.left

            # now perform the pop and compare follows inorder
            cur = tree_stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            # now if not  we can move the right
            cur = cur.right
# Time: O(N)
# Space: O(N)
    

    "recursive dfs inorder with array"

    # it will append into class var without returning anything
    # def dfs(self, root: Optional[TreeNode]) -> None:
    #     if not root: return

    #     # go to the  left most with inorder
    #     # we only need to call the funtion it will append the val in the class var so dont need to store their result.
    #     self.dfs(root.left)
    #     self.arr.append(root.val)
    #     self.dfs(root.right)

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     self.arr = []

    #     self.dfs(root)

    #     return self.arr[k-1]

# Time: O(N)
# Space: O(N) for the array