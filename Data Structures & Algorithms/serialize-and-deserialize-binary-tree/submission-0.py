# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Lesson:
    - Think about the BFS and DFS to build solution, most of the binary tree probs can be solved from there.
    - Always handling the base case first.

Solution:
    - Using the recursive preorder DFS to build the string and decode it.
"""

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # creating the array
        arr = []

        # creating the dfs preorder
        def dfs(root: Optional[TreeNode]) -> None:
            if not root: 
                arr.append('N')
                return

            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # construct array from str and create the pointer
        self.i = 0
        arr = data.split(',')
        
        # creating the recursive preorder dfs for constructing the tree
        def dfs() -> Optional[TreeNode]:
            
            if arr[self.i] == 'N': #remember to update pointer in None case too
                self.i += 1
                return None
            
            # after taking out the node then move the pointer 
            node_val = int(arr[self.i])
            node = TreeNode(node_val)
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()

