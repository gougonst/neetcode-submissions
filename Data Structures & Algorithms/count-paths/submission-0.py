class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(r: int, c: int) -> int:
            if r == m - 1 and c == n - 1:
                return 1
            elif r >= m or c >= n:
                return 0
            
            return dfs(r + 1, c) + dfs(r, c + 1)

        return dfs(0, 0)