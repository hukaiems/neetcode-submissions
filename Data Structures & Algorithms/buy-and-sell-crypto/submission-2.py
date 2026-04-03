class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high, if find lower then move that -> 2 pointers

        l, r = 0, 1
        res = 0
        while r < len(prices): # only need r -> loop through all the possible sell day
            # profitable ?
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            
            r += 1
        return res