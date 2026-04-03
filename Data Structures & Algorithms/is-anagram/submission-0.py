from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        anagram_hash = defaultdict(list)

        # sort the str so it has the correct order to become a key
        sorted_s = sorted(s)
        # append into hashmap
        sorted_t = sorted(t)

        if sorted_t == sorted_s:
            return True
        
        return False