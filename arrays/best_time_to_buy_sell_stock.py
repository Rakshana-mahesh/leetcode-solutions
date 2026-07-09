class Solution:
    def maxProfit(self, prices):
        lowest = prices[0]
        best_profit = 0
        
        for price in prices:
            if price < lowest:
                lowest = price
            else:
                profit = price - lowest
                if profit > best_profit:
                    best_profit = profit
        
        return best_profit