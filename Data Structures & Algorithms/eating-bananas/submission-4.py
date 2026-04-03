class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        "use the range k 1-> max to perform binary search"
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid_k = (r + l) // 2
            total_h = 0

            for p in piles:
                total_h += math.ceil(p / mid_k) # koko wait when there is time left
            
            if total_h <= h:
                res = min(res, mid_k)
                r = mid_k - 1 # still time left koko can eat slower
            else:
                l = mid_k + 1
            
        return res
# Time: O( logM * n) for m = max(piles) n = len(piles)
# Space: O(1)