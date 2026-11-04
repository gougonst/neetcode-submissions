class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for c in range(1, n):
            dp[c] = dp[c - 1] + grid[0][c]

        for r in range(1, m):
            dp[0] += grid[r][0]
            for c in range(1, n):
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]
        return dp[n - 1]