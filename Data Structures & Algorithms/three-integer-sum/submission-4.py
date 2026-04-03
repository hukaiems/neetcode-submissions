class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # so using sort to make it in order the use 2 pointers at first and last
        # like take advatage from the sorting list to increase and decrease the sum of 3 combination
        nums.sort()
        answer = set()

        # Listing through a list 
        for i in range(len(nums)):

            # first check to skip the duplicate like -1 -1 -1 0 1
            # i > 0 so it wont check nums[-1]
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            
            # initilize 2 pointers for searching combination
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if (nums[i] + nums[l] + nums[r] == 0):
                    # add in a set must put in immutable data which is tuple, etc
                    answer.add((nums[i], nums[l],  nums[r]))
                    # after add remember to move the left pointer to find the new combination
                    l += 1
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1

        return list(answer)

# Time: O(N^2)
# Space: O(N) because of the sorting 
