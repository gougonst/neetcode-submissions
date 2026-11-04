class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M, N = len(text1), len(text2)
        dp = [[-1] * (M) for _ in range(N)]

        def dfs(r: int, c: int) -> int:
            if r >= N or c >= M:
                return 0
            if dp[r][c] != -1:
                return dp[r][c]
            
            length = 0
            if text2[r] == text1[c]:
                length = 1 + dfs(r + 1, c + 1)
            else:
                length = max(dfs(r + 1, c), dfs(r, c + 1))
            dp[r][c] = length
            return dp[r][c]

        return dfs(0, 0)
