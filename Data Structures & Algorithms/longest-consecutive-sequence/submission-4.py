class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the first number in the sequence

        set_nums = set(nums)
        longest = 0

        # loop through the set to skip duplicate
        for n in set_nums:
            # confirm it's the first num in sequence
            if (n - 1) not in set_nums:
                length = 1
                while (n + length) in set_nums:
                    length += 1
                longest = max(longest, length)

        return longest
# TIme: O(N)
# Space: O(N)