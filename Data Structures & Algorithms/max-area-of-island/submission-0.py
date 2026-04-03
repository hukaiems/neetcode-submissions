class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # use normal iterative BFS with 4 directions in matrix

        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        max_area = 0
        row, col = len(grid), len(grid[0])

        # initilize the bfs
        def bfs(r: int, c: int) -> int:
            q = deque()
            temp_max = 1
            q.append((r, c))
            grid[r][c] = 0

            # the loop to run iterative bfs
            while q:
                r_cur, c_cur = q.pop()
                
                # now process move
                for dr, dc in directions:
                    r, c = r_cur + dr, c_cur + dc
                    if (r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0):
                        continue # continue cause this position is invalid
                    q.appendleft((r, c))
                    grid[r][c] = 0
                    temp_max += 1
            return temp_max
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    temp_max = bfs(r, c)
                    max_area = max(max_area, temp_max)
        
        return max_area