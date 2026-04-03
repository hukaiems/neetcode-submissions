class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # performing  binary search 2 times outside and in the founded array

        l, r = 0, len(matrix) - 1
        arr = []

        while l <= r:
            mid = ( r + l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]: # in the range
                arr = matrix[mid]
                break
            elif target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (r + l) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True

        return False
        