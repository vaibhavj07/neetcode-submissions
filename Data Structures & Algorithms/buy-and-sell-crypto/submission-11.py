class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        l = 0
        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
                r = l+1
        return maxProfit