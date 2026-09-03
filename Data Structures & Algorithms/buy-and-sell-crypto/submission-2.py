class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Sell price always larger than buy
        # n = len(prices)
        # profit = 0
        # for i in range (n):
        #     for j in range (i+1,n):
        #         if prices[i] < prices[j]:
        #             profit = max(profit, prices[j] - prices[i])
        # return profit

            buy = prices[0]
            profit = 0

            for price in prices:
                if price < buy:
                    buy = price
                else:
                    profit = max(profit, price - buy)

            return profit   



            
            