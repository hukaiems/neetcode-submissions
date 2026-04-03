class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sorted nums like 2 sum so we get advantage of the asc order list
        nums.sort()
        answer = set()

        for i in range(len(nums)):
            
            # Prevent it looping through the same index like -1 -1 -1 0 1
            # i > 0 so it wont use condition at the start of the list
            if( i > 0 and nums[i] == nums[i - 1]):
                continue    

            l = i + 1
            r = len(nums) - 1
       
            while l < r:

                if (nums[i] + nums[l] + nums[r] == 0):
                    answer.add((nums[i], nums[l], nums[r]))
                    l += 1
                # the sum is too small increase by move left pointer forward
                elif (nums[i] + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    r -= 1

        return list(answer)

# Time: O(N^2)
# Space: O(N) because of the sort algorithm


        # # Failed solution: --- there is a bug when it just auto increase the left pointer which by pass the value that can be used. 
        # # so using sort to make it in order the use 2 pointers at frist and last
        # nums = sorted(nums)
        
        # # build a nums_hash for faster look up
        # nums_hash = {}
        # for n in nums:
        #     # in the get find the value of thekey or just initilize 0 for it
        #     nums_hash[n] = 1 + nums_hash.get(n, 0)
        
        # print(nums_hash)
        # l = 0
        # r = len(nums_hash)
        # # curly braces is for set =)) and initilize empty set in python is used set()
        # # set only store immutable data
        # answer = set()
        # while l < r:
        #     print(f"NumsLeft:{nums[l]}")
        #     print(f"NumsRight:{nums[r]}")
        #     diff_num = - (nums[l] + nums[r])
        #     # check if the diff num is bigger than right  pointer, because right pointer is the biggest number
        #     # if it is bigger then move left pointer forward to reduce
        #     if( diff_num > nums[r]):
        #         l += 1
        #         continue
        #     # if equal check is there 2 values in the hash
        #     if (diff_num == nums[r]):
                
        #         if(nums_hash[nums[r]] == 2):
        #             answer.add((nums[l], diff_num, nums[r]))
            
        #     # if it is smaller than left pointer( which is the smallest number right now) pointer move right pointer backward
        #     if( diff_num < nums[l]):
        #         r -= 1
        #         continue
        #     # if equal check again
        #     if (diff_num == nums[l]):
        #         print(nums_hash[nums[l]])
        #         if(nums_hash[nums[l]] == 2):
        #             answer.add((nums[l], diff_num, nums[r]))  

        #     if( diff_num in nums_hash):
        #         answer.add((nums[l], diff_num, nums[r]))
                      
        #     l += 1

        # return list(answer)
