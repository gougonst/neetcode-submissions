class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                minPathSum = math.inf
                if r - 1 >= 0 and r - 1 < ROWS:
                    minPathSum = min(minPathSum, dp[r - 1][c])
                if c - 1 >= 0 and c - 1 < COLS:
                    minPathSum = min(minPathSum, dp[r][c - 1])
                minPathSum = 0 if minPathSum == math.inf else minPathSum
                dp[r][c] = grid[r][c] + minPathSum

        return dp[ROWS - 1][COLS - 1]