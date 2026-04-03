class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Solution:
        - Sliding window
        - Create 2 hashs and 2 vars have and need to keep track if we found 
            the sequence has all conditions meet which contains all the
                characters.

        """

        # initilize the hash map
        hash_t = defaultdict(int)
        hash_win = defaultdict(int)

        for c in t:
            hash_t[c] += 1
        
        # so need var is the letters in the t
        # satisfy all of the letters frequency
        have, need = 0, len(hash_t)
        res = [-1, -1] # because l, r start in 0 so initilize them -1
        min_len = float("infinity")

        # sliding window loop
        l = 0
        for r in range(len(s)):
            c = s[r]
            hash_win[c] += 1

            if c in hash_t and hash_win[c] == hash_t[c]: # if the c in hash and >= value then sastify 1 condition
                have += 1
            
            # condition if have == need then cal len and move l pointer until sequence invalid
            while have == need:
                cur_len = r-l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    res = [l, r]

                hash_win[s[l]] -= 1
                # check if the l element is in hash and make the condition fail
                if s[l] in hash_t and hash_win[s[l]] < hash_t[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        if min_len != float("infinity"): # mean we have found the sequence
            return s[l:r + 1] # remember it end at the before given index
        else:
            return ""



