class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        seen = set()
        ROW, COL = len(grid), len(grid[0])
        mins = -1 # cause when first add rotten and process it will be mins 0
        no_fresh_orange = True

        # now find all the 2 first
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    seen.add((r, c))
                    q.appendleft((r, c))
                if grid[r][c] == 1:
                    no_fresh_orange = False
        
        if no_fresh_orange:
            return 0

        def add_cell(r: int, c: int) -> None:
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                grid[r][c] != 1 or (r, c) in seen):
                return
            q.appendleft((r, c))
            seen.add((r, c))
        
        # now use the queue to process bfs
        while q:
            # now run through this first layer - process every adjacent cell of those cell has val 2
            for _ in range(len(q)):

                r, c = q.pop()
                grid[r][c] = 2 # turn into rotten

                # move 4 steps
                add_cell(r, c + 1)
                add_cell(r, c - 1)
                add_cell(r+1, c)
                add_cell(r-1, c)
            mins += 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1

        return mins
