"""
Lesson:
- Append a list is append the reference of that list so we need to append .copy()
- Only undo what I ran in backtracking so correct identation is very important.

Solution:
Build a backtracking algorithm base on 2 choices add or not add.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # need subset and res
        res = []
        subset = []

        # initilize backtracking
        def dfs(idx: int) -> None:
            # base case is out of index
            if idx >= len(nums):
                # append when base case
                res.append(subset.copy())
                return
            
            # we have 2 choices add or not 
            subset.append(nums[idx]) #add
            dfs(idx+1)

            subset.pop() #not add
            dfs(idx+1)
        
        dfs(0)
        return res

# Time: O(n * 2^n)  n is the length of the subset
# Space: O(n)