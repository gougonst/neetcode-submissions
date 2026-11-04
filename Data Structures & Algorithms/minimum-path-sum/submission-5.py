class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [0] * COLS
        dp[0] = grid[0][0]

        for c in range(1, COLS):
            dp[c] = grid[0][c] + dp[c - 1]

        for r in range(1, ROWS):
            dp[0] += grid[r][0]
            for c in range(1, COLS):
                dp[c] = grid[r][c] + min(dp[c], dp[c - 1])

        return dp[COLS - 1]