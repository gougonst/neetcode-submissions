class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        buyPrice = prices[0]
        maxValue = 0

        for i in range(1, len(prices)):
            price = prices[i]
            if buyPrice > price:
                # don't sell
                buyPrice = price
            elif buyPrice < price:
                # buy this day
                maxValue = max(maxValue, price - buyPrice)
        
        return maxValue