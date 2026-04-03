"""
Lesson:
- Carefully draw out the direction of backtracking to implement the code easier.

Solution:
    1. Backtracking + set() - My solution
        - Use a backtracking to run a for loop
        - Combine with hash set for comparing if it contains all values in the given list.
        - Wont have base case because the for loop will run out itself.

"""



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # we will use backtracking + set()

        res = []
        num_set = set(nums)
        size = len(nums)

        # initilize backtracking, we need cur to append and set to check legit
        def backtracking(cur: list, cur_set: set) -> None:
            for i in range(size):
                n = nums[i]
                if n not in cur_set:
                    cur_set.add(n)
                    cur.append(n)
                    # check legit
                    if cur_set == num_set:
                        res.append(cur.copy())
                    
                    # now backtracking
                    backtracking(cur, cur_set)
                    # remove explored path
                    cur.pop()
                    cur_set.remove(n)

        backtracking([], set())
        return res
