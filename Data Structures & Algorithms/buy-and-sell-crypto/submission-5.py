class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n  = len(prices)
        # profit = 0
        # for i in range (n):
        #     for j in range (i+1, n):
        #         profit = max(profit, prices[j]- prices[i])
        # return profit

        profit = 0
        min_price = prices[0]
        for sell in prices:
            profit = max(profit, sell - min_price)
            min_price = min(min_price, sell)
        return profit






        