class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create a set for faster look up
        nums_set = set(nums)
        max_len = 0

        # a for loop for processing
        for n in nums_set:
            # only work with starting number
            if (n-1 not in nums_set):
                length = 1
                # find all the number in the sequence 
                while (n + length in nums_set):
                    length += 1
                
                # compare to get the max length
                max_len = max(max_len, length)
        
        return max_len