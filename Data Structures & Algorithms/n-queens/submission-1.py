"""
Lesson:
- Pay close attention to figure the rule or formula for the solution condition.
- [] * n to duplicate the value inside a list n times.

Solution:
    - Backtracking + for loop
        - Base on 3 sets , col, PosDia, NegDia
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # board and res and 3 sets
        board = [['.'] * n for i in range(n)]
        res = []

        col, PosDia, NegDia = set(), set(), set()

        # backtrack
        def backtrack(r: int) -> None:
            # base case
            if r == n:
                board_copy = [''.join(row) for row in board]
                res.append(board_copy)
                return
            
            # for loop to find solution
            for c in range(n):
                # check valid
                if c not in col and (r+c) not in PosDia and (r-c) not in NegDia:
                    board[r][c] = 'Q'
                    col.add(c)
                    PosDia.add(r+c)
                    NegDia.add(r-c)
                    backtrack(r+1)

                    # delete
                    board[r][c] = '.'
                    col.remove(c)
                    PosDia.remove(r+c)
                    NegDia.remove(r-c)
        
        backtrack(0)
        return res
# Time: O(n!) because each time the choice decrease because the column lose 1 position.
# Space: O(N^2) for the board when running algorithm
            
