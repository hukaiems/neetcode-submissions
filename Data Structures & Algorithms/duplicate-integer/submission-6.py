class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsets = [];

        for n in nums:
            if (n in hashsets):
                return True;
            hashsets.append(n);
        
        return False;

            