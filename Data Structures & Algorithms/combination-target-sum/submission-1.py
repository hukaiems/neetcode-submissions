"""
Lesson:
- tuple() to turn into tuple in python.
- Validating the backtracking carefully so it won't make duplicate exploration.

Solution:
    1. Backtracking with 2 decisions add or never touched added value
"""

class Solution:
    # for my OOP
    # initilize the backtracking
    def dfs(self, total: int, i: int, com: list) -> None:
        # base case > target
        if total == self.target:
            self.res.append(com.copy()) # the snap of com not reference
            return #remember to return so it wont run and causing wrong answer
        if total > self.target or i >= len(self.nums):
            return
        
        # 2 choices
        # add choice
        com.append(self.nums[i])
        total += self.nums[i]
        self.dfs(total, i, com)
        n = com.pop()
        total -= n

        self.dfs(total, i+1, com) # never touched choice

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # it needs nums, tar, res
        self.nums = nums
        self.target = target
        self.res = []

        self.dfs(0, 0, [])
        return self.res

# Time: O(2^(t/m)) 2 for 2 choices, t = target, m = smallest value the worst case is total of smallest case > target
# Space: O(t/m) because the max height is max append in the list and max height of the recursion which is the tree height