class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx = 0

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# Time: O(N) -> loop through once
# Space: O(N) -> for the hash set