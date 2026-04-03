class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using 2 pointers to find sum
        # because it is ascending
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_n = numbers[l] + numbers[r]
            if sum_n > target:
                r -= 1
            elif sum_n < target:
                l += 1
            else:
                return [l+ 1, r+ 1]
        # no need to return anything else due to there is always an anser
# TIme: O(N)
# Space: O(1)
