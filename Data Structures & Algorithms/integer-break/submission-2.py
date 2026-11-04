class Solution:
    def integerBreak(self, n: int) -> int:
        # dp: Maximum product with i
        dp = [0] * (n + 1)

        def dfs(num: int) -> int:
            if dp[num] != 0:
                return dp[num]

            dp[num] = 0 if num == n else num
            for i in range(1, num // 2 + 1):
                j = num - i
                dp[num] = max(dp[num], dfs(i) * dfs(j))
            return dp[num]

        return dfs(n)