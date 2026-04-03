class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using 2 pointers at first and last index of the list
        # because of the sorted array we can decrease or increase the sum of 2 pointers
        # simply by moving the left pointer forward to increase the sum
        # or moving the right pointer backward to decrease the sum

        l = 0
        r = len(numbers)- 1

        # while loop run until 2 pointers meet each other
        while l < r:
            if(numbers[l] + numbers[r] == target):
                return [l + 1, r+1]
            # if bigger then we have to decrease the sum by move right pointer backward in the sorted array
            elif (numbers[l] + numbers[r] > target):
                r -= 1
            else:
                l += 1

# Time: O(N)
# Space: O(1)
