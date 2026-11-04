class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        # dp: Maximum product with i
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        def dfs(num: int) -> int:
            if dp[num] != 0:
                return dp[num]

            for i in range(1, num // 2 + 1):
                j = num - i
                dp[num] = max(dp[num], dfs(i) * dfs(j))
            return dp[num]

        return dfs(n)