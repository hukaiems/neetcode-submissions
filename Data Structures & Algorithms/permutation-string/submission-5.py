class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # we will use 2 hashmap to compare
        # alphabet only has 26 characters so we can compare permutation using 2 hashmap
        # base on the sliding window technique

        # base case
        if len(s1) > len(s2): return False

        # create the hashmap
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        hash_1 = {char: 0 for char in alphabet}
        hash_2 = hash_1.copy()

        # now fill the hash_1
        for i in range(len(s1)):
            hash_1[s1[i]] += 1
            hash_2[s2[i]] += 1
        
        # begin sliding window
        l = 0
        for r in range(len(s1), len(s2)): # start from the s1 end
            if hash_1 == hash_2:
                return True
            
            hash_2[s2[r]] += 1
            hash_2[s2[l]] -= 1
            l += 1

        if hash_1 == hash_2:
            return True
        return False