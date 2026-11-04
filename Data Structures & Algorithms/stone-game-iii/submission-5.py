class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            cur = 0
            dp[i] = -math.inf
            for j in range(i, min(i + 3, n)):
                cur += stoneValue[j]
                dp[i] = max(dp[i], cur - dp[j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"