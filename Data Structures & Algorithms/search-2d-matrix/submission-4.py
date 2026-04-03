class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # ... your comments ...

        # --- THIS IS THE FIX ---
        # Search from index 0 to the last valid index
        l, r = 0, len(matrix) - 1
        row = -1 # You had a bug here, you should return False if no row is found
        
        while l <= r:
            mid = (r + l) // 2
            
            # This is a small bug fix: if there's only one row, l and r might be the same
            # but you still need to set the row.
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target: # Use -1 for last element, it's safer
                l = mid + 1
            else: # This case is now handled by the check above
                row = mid
                break # Found the potential row
        
        if row == -1:
            return False
            
        # --- AND THIS IS THE SECOND FIX ---
        # Search from index 0 to the last valid index
        l, r = 0, len(matrix[0]) - 1 
        
        while l <= r:
            mid = (r + l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False