from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases
        if len(s) != len(t):
            return False

        s_hashmap = defaultdict(int)
        t_hashmap = defaultdict(int)

        for c in s:
            s_hashmap[c] += 1
        
        for c in t:
            t_hashmap[c] += 1

        if s_hashmap == t_hashmap:
            return True
        return False