class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def dfs(num) -> int:
            if num == 0:
                return 0
            if num in dp:
                return dp[num]
            if num ** 0.5 == int(num ** 0.5):
                dp[num] = 1
                return dp[num]

            i = 1
            minReq = math.inf
            while i * i < num:
                remain = num - i * i
                minReq = min(minReq, 1 + dfs(remain))
                i += 1
            dp[num] = minReq
            return dp[num]

        dfs(n)
        return dp[n]
