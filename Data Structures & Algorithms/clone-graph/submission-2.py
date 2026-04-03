"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Lesson:
- N + E is big O time in graphs.

"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen_hash = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            new_node = Node(node.val)
            seen_hash[node.val] = new_node
            for nei in node.neighbors:
                if nei.val not in seen_hash:
                    dfs(nei)
                new_node.neighbors.append(seen_hash[nei.val])

            return new_node
        
        return dfs(node) if node else None