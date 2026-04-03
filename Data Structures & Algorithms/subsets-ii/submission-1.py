"""
Lesson:
- defaultdict will initilize for us we just use it normally.
- A pattern: sort and loop to skip duplicate, running with backtracking + idx only.

Solution:
    1. Backtracking + hash(set)
        - hash(set): key(size of com)-value:(combination_set)
    
    2. Backtracking + skip duplicate loop
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # initilize result and sorting
        res = []
        nums.sort()

        # backtracking
        def backtrack(cur: list, idx: int) -> None:
            # check base case out of idx
            if idx == len(nums): # append the cur
                res.append(cur.copy())
                return
            
            n = nums[idx]
            #  2 choices backtrack, append or not
            cur.append(n)
            backtrack(cur, idx + 1)
            cur.pop()

            # skip duplicate
            while idx+1 < len(nums) and n == nums[idx+1]:
                idx += 1
            backtrack(cur, idx+1)
        
        backtrack([], 0)
        return res







# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         nums.sort()
#         res = [[]]
#         exist = defaultdict(set)

#         def backtrack(cur: list, idx: int) -> None:

#             #  a loop
#             for i in range(idx, len(nums)):
#                 n = nums[i]
#                 cur.append(n)
#                 size = len(cur)
#                 # check legit check size first then combination itself
#                 if size not in exist:
#                     exist[size].add(tuple(cur))
#                     res.append(cur.copy())
#                 elif tuple(cur) not in exist[size]:
#                     exist[size].add(tuple(cur))
#                     res.append(cur.copy())

#                 backtrack(cur, i+1)
#                 cur.pop()
        
#         backtrack([], 0)
#         return res
# Time: O(N * 2^N) for N is the number elements.
# Space: O(N * 2^N)