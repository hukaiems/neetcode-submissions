"Reimplement BFS"
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen_set = set()
        ROW, COL = len(grid), len(grid[0])
        q = deque() # queue to run BFS
        distance = 0

        # now append all zero into queue (all treasure cells)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.appendleft((r, c))
                    seen_set.add((r, c))
        
        def add_step(r: int, c: int) -> None:
            # check valid cell
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                grid[r][c] == -1 or (r, c) in seen_set):
                return
            # if valid then append
            q.appendleft((r, c))
            seen_set.add((r, c))
        
        # run bfs
        while q:
            # pop it out to process
            for _ in range(len(q)):
                r, c = q.pop() # at this stage this current cell has been added to seen so we find the 4 adjacent cells
                grid[r][c] = distance # updating the new distance for this cell first then find 4 new cells
                
                # 4 steps
                add_step(r, c+1)
                add_step(r, c-1)
                add_step(r-1, c)
                add_step(r+1, c)

            # update the distance
            distance += 1


           



"Try to implement BFS, trying to process each iteration of bfs is the cell has ascending distance to those gate."
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         seen_set = set()
#         ROW, COL = len(grid), len(grid[0])
#         q = deque()
#         distance = 0 # we will process distance in increasing order

#         # for loop to take out all 0 cell
#         for r in range(ROW):
#             for c in range(COL):
#                 if grid[r][c] == 0:
#                     q.appendleft((r, c))
#                     seen_set.add((r,c))
        
#         # this one use to check is the cell valid to add in the queue for processing.
#         def add_queue(r: int, c: int) -> None:
#             if (r < 0 or c < 0 or r >= ROW or c >= COL or
#                 (r, c) in seen_set or grid[r][c] == -1): # we will process from those 0 cell so if it the wall then we dont touch
#                 return
#             q.appendleft((r, c))
#             seen_set.add((r,c))


#         # while q loop processing BFS
#         while q:
#             # now process each layer of distance
#             for _ in range(len(q)):
#                 r, c = q.pop()
#                 grid[r][c] = distance
                
#                 # add in 4 directions into the queue using helper function.
#                 add_queue(r, c - 1)
#                 add_queue(r, c + 1)
#                 add_queue(r - 1, c)
#                 add_queue(r + 1, c)

#             distance += 1
# Time: O(M* N)
# Space: O(M * N)


"This solution is backtracking using recursive DFS + seen set and a temp_min to track down the min val."
"But the solution got time limit."
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#         # basically we will need to use recursive dfs for every step
#         row, col = len(grid), len(grid[0])
#         inf_num = 2147483647
#         seen_set = set()

#         def dfs(r: int, c:int, temp_min: int) -> int:
#             # base case
#             if (r < 0 or c < 0 or r >= row or c >= col or
#                 grid[r][c] == -1 or (r, c) in seen_set ):
#                 return float('inf')


#             if grid[r][c] == 0:
#                 return 0

#             temp_min = 1 
#             seen_set.add((r, c))
#             # now move the step
#             move_left = dfs(r, c-1, temp_min)

#             move_down = dfs(r+1, c, temp_min)
            
#             move_right = dfs(r, c+1, temp_min)

#             move_up = dfs(r-1, c, temp_min)
            
#             temp_min = min(temp_min + move_left, temp_min + move_right, temp_min + move_down, temp_min + move_up)

#             seen_set.remove((r,c))

#             return temp_min



#         for r in range(row):
#             for c in range(col):
#                 if grid[r][c] == inf_num:
#                     temp_min = dfs(r, c, float('inf'))
#                     grid[r][c] = temp_min

#         return None