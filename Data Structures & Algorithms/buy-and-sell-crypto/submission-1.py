class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Sell price always larger than buy
        n = len(prices)
        profit = 0
        for i in range (n):
            for j in range (i+1,n):
                if prices[i] < prices[j]:
                    profit = max(profit, prices[j] - prices[i])
        return profit
                
            
            