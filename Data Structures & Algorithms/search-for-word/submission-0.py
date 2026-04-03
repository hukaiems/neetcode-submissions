"""
Lesson:
- DFS is a specific form of BackTracking. DFS will go as deep as possible like Backtracking.
- With many wrong condition, we can combine every cases in 1 line condition. 
- We can use as many or/and as we need in an if condition.

Solution:
Using backtracking to go to each element in the board and apply back tracking
    to go as deep as possible and find the correct answer. 
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we need a set storing known path
        path = set()
        # we need the len of cols and rows
        len_row, len_col = len(board), len(board[0])

        # now we will build a backTracking algorithm
        def backTracking(idx: int, i: int, j: int) -> bool:
            # it will check if the current node is the last node of the word first
            if idx == len(word):
                return True
            
            # now if not then check if the new path legit
            if (i < 0 or j < 0 or
                i >= len_row or j >= len_col or
                board[i][j] != word[idx] or
                (i, j) in path):
                return False #bad path
            
            # if the path is legit then take it and check new path
            path.add((i, j))
            # we only need 1 of the path to correct
            res = (backTracking(idx+1, i - 1, j) or
                    backTracking(idx+1, i, j-1) or
                    backTracking(idx+1, i+1, j) or
                    backTracking(idx+1, i, j+1) )
            # remember to prune or cut off the path before return
            # so that we return the state of this path meaning we have found any possible path now we return
            # so you can move on to the new path and do the exploration
            path.remove((i, j))
            return res

        # use the backtracking to eplore every possible path 
        for i in range(len_row):
            for j in range(len_col):
                if backTracking(0, i, j): #only need 1 win only 1 yia yiaa
                    return True
        
        # if the loop finish meaning nothing found return False
        return False

# Time: O(m * n * 4^ l) for l is the len of word
# Time: O( N) for n is the recursion stack
        