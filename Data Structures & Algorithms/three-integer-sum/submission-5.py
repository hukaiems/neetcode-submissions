"""
Lesson:
- Analyze brute force inefficient, from there we can know what to optimize
- 2 pointers will have 2 ways, start at same side or both sides

Pattern:
Generating combination without duplicate
- We can sort and have a loop to skipp all the duplicate.
- Also if found combination we can use 2 pointers too.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # 2 pointers
        # loop to choose first value
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue  # move on when we at the duplicate value
            
            # now we can use 2 pointers
            l, r = i + 1, len(nums)-1
            while l < r:
                three_sum = a + nums[l] + nums[r] # if com > 0 then decrease else increase because list is sorted
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else: # if found then append
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # now skip duplicate for l and loop to find the next value
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
# Time: O(N^2) for 2 nested loop
# Space: O(n) for sorting algorithm
                    





# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         # so using sort to make it in order the use 2 pointers at first and last
#         # like take advatage from the sorting list to increase and decrease the sum of 3 combination
#         nums.sort()
#         answer = set()

#         # Listing through a list 
#         for i in range(len(nums)):

#             # first check to skip the duplicate like -1 -1 -1 0 1
#             # i > 0 so it wont check nums[-1]
#             if(i > 0 and nums[i] == nums[i-1]):
#                 continue
            
#             # initilize 2 pointers for searching combination
#             l = i + 1
#             r = len(nums) - 1
#             while l < r:
#                 if (nums[i] + nums[l] + nums[r] == 0):
#                     # add in a set must put in immutable data which is tuple, etc
#                     answer.add((nums[i], nums[l],  nums[r]))
#                     # after add remember to move the left pointer to find the new combination
#                     l += 1
#                 elif (nums[i] + nums[l] + nums[r] < 0):
#                     l += 1
#                 else:
#                     r -= 1

#         return list(answer)

# Time: O(N^2)
# Space: O(N) because of the sorting 
