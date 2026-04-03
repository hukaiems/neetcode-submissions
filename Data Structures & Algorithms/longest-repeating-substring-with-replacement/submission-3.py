class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        - Rule: result = len - max_f <= k
        """


        # using sliding window create from 2 pointers
        # sliding window

        l = res = max_f = 0
        hash_map = defaultdict(int)

        # slide window through
        for r in range(len(s)):
            hash_map[s[r]] += 1
            max_f = max(max_f, hash_map[s[r]])

            # check condition
            while (r - l + 1) - max_f > k: # update freq and move left pointer
                hash_map[s[l]] -= 1
                l += 1

            # now check result when condition is satisfied
            # note: using only max_f will create satified condition but technically wrong when there are no new max_f
            res = max(res, r - l + 1)
        
        return res