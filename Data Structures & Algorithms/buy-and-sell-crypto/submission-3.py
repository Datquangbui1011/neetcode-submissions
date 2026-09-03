class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # n = len(prices)
        
        # for i in range (n):
        #     for j in range (i+1, n):
        #         if prices[j] > prices[i]:
        #             profit = max(profit, prices[j]-prices[i])
        # return profit


        buy = float('inf')
        profit = 0
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)
        return profit