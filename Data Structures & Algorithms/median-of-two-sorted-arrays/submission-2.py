class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        # if we choose longer array we can cause the j when computing 
        #    j = half - i - 2 become too negative or positive which make it out of index range
        if len(B) < len(A):
            A, B = B, A # python magic =))
        
        total = len(A) + len(B)
        half = total // 2

        # perform BS on the shorter array
        l, r = 0, len(A) - 1
        while True:
            i = (r + l) // 2
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float("-infinity")
            ARight = A[i + 1] if i +  1 < len(A) else float("infinity")
            BLeft = B[j] if j >= 0 else float("-infinity")
            BRight = B[j+1] if j + 1 < len(B) else float("infinity")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1

# Time: O(log(min(m + n)))
# Space: O(1)