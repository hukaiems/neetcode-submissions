from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # create rows cols and squares(big 3x3) using dict(set)
        # dict is for faster look up and set is storing only unique things
        # now with it if it is duplicate we can return False immediately

        rows = defaultdict(set)
        cols = defaultdict(set)
        # this one will store key are a pair of row index //3 and column index //3
        squares = defaultdict(set)

        # only way i know now to run through 2 d matrix are 2 for loop
        for r in range(9):
            for c in range(9):
                # we will skip the dot and process with number
                if board[r][c] == '.':
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[r//3, c//3]):
                    return False
            
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])    
                
        return True