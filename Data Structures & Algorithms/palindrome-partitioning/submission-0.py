"""
Lesson:
- Trying to think about how to explore each possible solution in each backtracking turn.
- Think about how the possible solution can be found using which condition or mechanism...

Intuition:
- Each character is a palindrome.
- Only move on if we found a palindrome in that branch.

Solution:
Backtracking + for loop
- Use a for loop to traverse each path

"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # initilize the res and part
        res = []
        part = []

        # backtrack
        def backtrack(idx: int) -> None:
            # if base case
            if idx >= len(s):
                res.append(part.copy())
                return
            
            # a for loop to explore
            for j in range(idx, len(s)):
                # only move on if found palindrome
                if self.isPalin(s, idx, j):
                    # if yes then append to part
                    part.append(s[idx:j+1])
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
    # helper method
    def isPalin(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# Time: O(N * 2^N) 2^N for the subset which is the node in the tree.
# Space: O(N)