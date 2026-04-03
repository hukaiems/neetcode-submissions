class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
        2 binary searchs for rows and cols

        Lesson:
        - If middle pointer not bigger or smaller than target
            It mean middle pointer == target.
        """

        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1

        # first binary search to find the row contains target
        l , r = 0, ROWS
        # initilize a row = -1 so that if it isnt find the correct row then -1 is kept and return False
        row = -1
        while l <= r:
            # find the middle row
            mid = (r + l) // 2

            # if middle row not contains target shift it
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            # if middle row not bigger or smaller than target than it contains target
            else:
                row = mid
                # add a break to tell yeh we found it 
                break
        # cant find correct row
        if row == -1:
            return False
        # binary search for cols
        l , r = 0, COLS
        while l <= r:
            mid = (r+l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
        

# Time: O(log(M * N))
# Space: O(1)