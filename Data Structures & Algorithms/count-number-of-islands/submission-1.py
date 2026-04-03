"""
Lesson:
- Figuring out list of step can take, usually matrix only has 4 steps to move.

Solution:
    1. BFS iteration + hash set ( or not)
        - BFS will find all the land in that islands
        - After BFS return increase islands count by 1.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        row, col = len(grid), len(grid[0])
        islands = 0

        def bfs(r: int, c: int) -> None:
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                # pop the position out
                r_cur, c_cur = q.pop()
                for dr, dc in directions:
                    r, c = r_cur + dr, c_cur + dc
                    # check if invalid pos continue
                    if (r < 0 or r >= row or 
                        c < 0 or c >= col or
                        grid[r][c] == '0'):
                        continue
                    q.appendleft((r, c))
                    grid[r][c] = '0'
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands

# Time: O(M*N) for row and col each cell will be only process one
# Space: O(A) for all entities
        