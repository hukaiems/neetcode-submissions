"""
Lesson:
- Trie is a data structure like tree but efficiently storing characters.
- A Trie Node contains a hash to store children node and a boolen
    to check if the current node is the end of a word.
- Time complexity of Trie Node is O(L) for the length of word or prefix.
"""

class TrieNode:
    def __init__(self): # self for python to identify which object to work on
        self.children = {}
        self.isTheEnd = False

class PrefixTree:

    def __init__(self):
        # we only need the root
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # check if exist if not then create and insert
        # we need a pointer to track
        cur = self.root
        for c in word:
            if c not in cur.children:
                node = TrieNode()
                cur.children[c] = node
            
            # if it is then just move
            cur = cur.children[c]
        
        # if the end then set bool
        cur.isTheEnd = True

        print(self.root.children)


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
        
            cur = cur.children[c]
        
        # now we out of the loop which means we find the word
        # return the boolen of current node to make sure this is the end
        return cur.isTheEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        # if it out of the loop
        # which mean the whole prefix is in the Trie
        # we simply return True
        return True
        