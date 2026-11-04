class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [-math.inf] * (n + 2)
        dp[-1] = 0
        dp[-2] = 0
        dp[-3] = 0

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                A = prices[j] - prices[i] + dp[j + 2]
                B = dp[i + 1]
                dp[i] = max(A, B, dp[i])
        return dp[0]