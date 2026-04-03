class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Solution 1 using 2 pointers with funtion
        l = 0
        r = len(s) - 1

        # a while loop stop when l >= r
        while l < r:
            # check is it alphaNum
            # if I want to use the method for a nother method inside a class
            # have to tell it so it know where to look up with self.
            while(l < r and not self.isAlphaNum(s[l]) ):
                l += 1
            while(r > l and not self.isAlphaNum(s[r])):
                r -= 1
            
            # compare 2 pointers
            if (s[l].lower() != s[r].lower()):
                return False
            l += 1
            r -= 1

        return True


    def isAlphaNum(self, c: str):
        # using raw string for this task, match anything inside the bracket
        pattern = r'[a-z0-9]'

        # this one hmmm i think that is more than O(N) depends
        if re.search(pattern, c.lower()): 
            return True
        else:
            return False


# Time: O(N)
# Space O(1)