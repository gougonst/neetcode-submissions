class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, sold, cooled = -math.inf, 0, 0

        for price in prices:
            buy = max(bought, cooled - price)
            cool = max(cooled, sold)
            sell = price + bought

            bought, sold, cooled = buy, sell, cool
        return max(cooled, sold)