class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = l+ 1
        max_profit = 0
        # 2 pointers 
        while r < len(prices):
            if prices[r] < prices[l]:
                # found the lower price
                l = r
                r += 1
                # move 2 pointers and continue
                continue
            
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            r += 1
        
        return max_profit