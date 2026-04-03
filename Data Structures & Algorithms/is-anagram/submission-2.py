class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        "use a hash map for both"

        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        
        for c in s:
            s_hash[c] += 1

        for c in t:
            t_hash[c] += 1

        if s_hash == t_hash:
            return True
        else:
            return False
# O(N)
# O(N)

        # # sort the str so it has the correct order to become a key
        # sorted_s = sorted(s)
        # # append into hashmap
        # sorted_t = sorted(t)

        # if sorted_t == sorted_s:
        #     return True
        
        # return False
# Time: O(NlogN)
# Space: O(N)