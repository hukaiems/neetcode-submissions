class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using 2 pointers with isalnum to check correct alphabet
        
        l, r = 0, len(s) - 1
        while l < r:
            # check alpha 
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # now compare
            if s[l].lower() != s[r].lower():
                return False
            
            # move the pointers
            l += 1
            r -= 1
        return True