import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        Lesson:
        - Pay attention to answer range or range of data structure.
        - Compare 2 constant data structures is O(1)

        Solution:
        - Create 2 hashMap to compare.
        - Hash map only contains 26 chars, a-z.
        """

        # check if s1 > s2
        if len(s1) > len(s2):
            return False

        # create 2 hashMaps, 1 for s1 and 1 for sliding window
        # initilize hash map to have full a-z key
        hash1 = dict.fromkeys(string.ascii_lowercase, 0)
        hash_window = dict.fromkeys(string.ascii_lowercase, 0)

        # initilize the s1 in hash1 and first window in hash_window
        for i in range(len(s1)):
            hash1[s1[i]] += 1
            hash_window[s2[i]] += 1

        # sliding window loop
        l = 0
        for r in range(len(s1), len(s2)):
            if hash1 == hash_window:
                return True
            
            hash_window[s2[l]] -= 1 # decrease the left pointer element
            l += 1
            hash_window[s2[r]] += 1 # increase the right pointer element
        print(hash_window)
        # last check, because the hash_window still need last element
        if hash1 == hash_window:
            return True
        return False

# Time: O(N)  compare hash is constant 26 so just O(1)
# Space: O(1)