class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        USing sliding window - 2 pointers:
        - Looping through a data structure doesnt mean it is O(N).
        - Trick is to keep the max_f without updating when it decrease.
            Because every outlier sequence shorter than max_f wont matter.
        """
        l, r = 0, 0

        max_len = 0
        max_f = 0
        hashMap = defaultdict(int) #auto initilize 0

        while r < len(s):
            # immediately append into dict
            hashMap[s[r]] += 1
            # check to see if new append value higher then max_f
            max_f = max(max_f, hashMap[s[r]])

            while (r-l + 1) - max_f > k:
                hashMap[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r - l + 1))
            r += 1

        return max_len
