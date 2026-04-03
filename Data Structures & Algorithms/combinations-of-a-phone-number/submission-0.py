"""
Lesson:
- Handling string number carefully.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # inilize the res and sub
        res = []
        sub = []

        # hashMap
        hashMap = {}
        hashMap[1] = []
        hashMap[2] = ['a', 'b', 'c']
        hashMap[3] = ['d', 'e', 'f']
        hashMap[4] = ['g', 'h', 'i']
        hashMap[5] = ['j', 'k', 'l']
        hashMap[6] = ['m', 'n', 'o']
        hashMap[7] = ['p', 'q', 'r', 's']
        hashMap[8] = ['t', 'u', 'v']
        hashMap[9] = ['w', 'x', 'y', 'z']

        if len(digits) < 1:
            return res

        # backtrack
        def backtrack(idx_digit: int) -> None:
            # base case
            if len(sub) >= len(digits):
                res.append("".join(sub))
                return
            
            # for loop, take out the value in the hash
            key = int(digits[idx_digit])
            for i in range(len(hashMap[key])):
                sub.append(hashMap[key][i])
                backtrack(idx_digit + 1)
                sub.pop()

        backtrack(0)
        return res

