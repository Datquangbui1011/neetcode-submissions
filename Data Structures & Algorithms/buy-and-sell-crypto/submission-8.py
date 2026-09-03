class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_profit = prices[0]
        for price in prices:
            profit = max(profit, price - min_profit)
            min_profit = min(min_profit, price)
        return profit
            