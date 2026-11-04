class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]
        memo[m - 2][n - 1] = 1
        memo[m - 1][n - 2] = 1

        def dfs(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            elif r >= m or c >= n:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            
            memo[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[r][c]

        return dfs(0, 0)