
"""
Lesson:
- stack.values() to access value in a dict.
- Design the return statement to optimize the recursive time complexity.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    # creating normal Trie
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                node = TrieNode()
                cur.children[c] = node
            cur = cur.children[c]
        
        # remember to update bool of last word
        cur.word = True
        
    #  now we need to tweak it a little bit
    # we will use recursive to take all the element when we meet dot 
    # we will go down each path and check, only need 1 path return true
    def search(self, word: str) -> bool:
    
        def dfs(idx: int, root: Optional[TrieNode]) -> bool:
            cur = root
            # we need to change this to index so we can turn to recursive
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    # now when we meet the dot
                    # we will traverse through every value in the current hash to check the next word
                    for child in cur.children.values():
                        # so to access next element is i+1, and pass down the net node to check their children
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word
        return dfs(0, self.root)
