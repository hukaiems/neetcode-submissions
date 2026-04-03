"""
Lesson:
- Defaultdict can help to build a hash of list more easily.
- BackTracking can be used without the need to return anything.
- Remember to delete the path that backTracking has just explored to move to the next exploration.
"""

# Initilize a TrieNode class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def addWord(self, word: str) -> None:
        cur = self # the pointer will point to the Trie node object

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True # initilize True for last word

# now use backtracking with Trie
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # we need 1. res, path ; 2. boundaries ; 3. the Trie
        res, path = set(), set()
        len_row, len_col = len(board), len(board[0])
        root = TrieNode() 

        # add words into Trie =)))
        for w in words:
            root.addWord(w)

        # initilize the backTracking
        def backTracking(i: int, j: int, node: Optional[TrieNode], word: str) -> None:
            # check legit step
            if ( i < 0 or j < 0 or
                i >= len_row or j >= len_col or #in boundaries
                board[i][j] not in node.children or  # exist in the node hash
                (i, j) in path):  # must be a new step
                return False
            
            # legit then add 
            path.add((i, j)) # move this new to the path
            word += board[i][j]
            node = node.children[board[i][j]]
            if node.word:
                res.add(word)
            
            # now continue exploring
            backTracking(i - 1, j, node, word)
            backTracking(i + 1, j, node, word)
            backTracking(i, j - 1, node, word)
            backTracking(i, j + 1, node, word)

            # please remove after you explored in backTracking
            path.remove((i, j))

        # now begin to do backTracking for each step
        for i in range(len_row):
            for j in range(len_col):
                backTracking(i, j, root, "")
        
        return list(res)

# Time: O(M * N * 4*3^(t-1) + s) for t is the length of longest word and s is the sum of all word length
# Space: O(S + H)