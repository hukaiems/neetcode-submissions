class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashsets = set()

        for n in nums:
            if (n in hashsets):
                return True;
            hashsets.add(n);
        
        return False;

            