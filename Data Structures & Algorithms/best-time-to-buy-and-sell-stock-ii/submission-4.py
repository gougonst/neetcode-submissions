class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(0, len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                maxProfit += profit
        return maxProfit