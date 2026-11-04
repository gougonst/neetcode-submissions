class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        dp = [0] * (abs(n) + 1)

        def dfs(x: int, n: int) -> int:
            if n <= 0:
                return 1
            if dp[n] != 0:
                return dp[n]

            val = dfs(x, n // 2) * dfs(x, n // 2)
            if n % 2:
                val *= x

            dp[n] = val
            return dp[n]
        
        val = dfs(x, abs(n))
        
        return val if n > 0 else 1 / val

    