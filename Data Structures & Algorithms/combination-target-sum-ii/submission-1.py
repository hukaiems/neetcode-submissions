"""
Lesson:
- Easier to solve backtracking by drawing the decision tree.
- .sort() is for list only, sort in place and return None, sorted() is for any data structures.


Solution:
- 2 choices backtracking with a loop to skip duplicate in a sorted list.
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # inilize res, sorted array
        res = []
        nums = sorted(candidates)

        # 2 choices backtracking
        def backtracking(i: int, cur: list, total: int) -> None:
            # base case > target
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(nums): # becareful when i > len(nums)
                return
            
            # 2 choices, 1 add
            cur.append(nums[i])
            total += nums[i]
            backtracking(i + 1, cur, total) #i + 1 because we cant use a same val twice
            cur.pop()
            total -= nums[i]

            # 2 never touch it, remember to skip the duplicate
            while i+1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i+1, cur, total)

        # now run backtracking and return
        backtracking(0, [], 0)
        return res
# Time: O(N * 2^N) n is the length of candidates, first n is for copying time when in case like copy more than half candidates
# Space: O(N)