class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # profit = 0
        # for i in range(n):
        #     sell = prices[i]
        #     for j in range (i+1, n):
        #         buy = prices[j]
        #         profit = max(profit, buy-sell)
        # return profit

        profit = 0
        min_price = prices[0]
        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        return profit

