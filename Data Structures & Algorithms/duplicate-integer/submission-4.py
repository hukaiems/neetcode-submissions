class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_array = [];
        for i in range(len(nums)):
            for j in range(len(duplicate_array)):
                if(nums[i] == duplicate_array[j]):
                    return True;
            duplicate_array.append(nums[i]);
        
        return False;
            