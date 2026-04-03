class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        Lesson:
        - can use the char still in set condition
            to delete from left pointer (left most until del the char in set)
        """


        l = 0
        max_len = 0
        # a set to keep unique element and the len
        charSet = set()

        for r in range(len(s)):
            if s[r] in charSet:
                # use condition char still in set to delete left most value until delete the char
                while s[r] in charSet: 
                    charSet.remove(s[l])
                    l+= 1

            charSet.add(s[r])
            cur_len = len(charSet)
            max_len = max(max_len, cur_len)

        return max_len