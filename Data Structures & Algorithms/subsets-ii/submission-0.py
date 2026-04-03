"""
Lesson:


Solution:
    1. Backtracking + hash(set)
        - hash(set): key(size of com)-value:(combination_set)
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = [[]]
        exist = defaultdict(set)

        def backtrack(cur: list, idx: int) -> None:

            #  a loop
            for i in range(idx, len(nums)):
                n = nums[i]
                cur.append(n)
                size = len(cur)
                # check legit
                if size not in exist:
                    exist[size].add(tuple(cur))
                    res.append(cur.copy())
                elif tuple(cur) not in exist[size]:
                    exist[size].add(tuple(cur))
                    res.append(cur.copy())
                backtrack(cur, i+1)
                cur.pop()
        
        backtrack([], 0)
        return res
