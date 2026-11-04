class Solution:
    def integerBreak(self, n: int) -> int:
        # dp: Maximum product with i
        dp = {}

        def dfs(num: int) -> int:
            if num in dp:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num // 2 + 1):
                j = num - i
                dp[num] = max(dp[num], dfs(i) * dfs(j))
            return dp[num]

        return dfs(n)