class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 0

        profit = 0
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                buy = prices[i]
                sell = prices[j]
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit

                
        if max_profit <= 0:
            return 0

        return max_profit



        