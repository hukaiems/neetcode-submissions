from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_hash = defaultdict(list)

        for w in strs:
            temp_hash = [0] * 26
            for c in w:
                temp_hash[ord(c) - ord('a')] += 1
            
            
            big_hash[tuple(temp_hash)].append(w)
        
        return list(big_hash.values())
                