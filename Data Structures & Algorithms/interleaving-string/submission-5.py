class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if len(s3) != m + n:
            return False

        s1 = "#" + s1
        s2 = "#" + s2
        s3 = "#" + s3
        # dp: n+1 * m+1, s2 * s1
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and s2[i] == s3[i]
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i  -1] and s1[i] == s3[i]

        for i in range(1, n + 1):
            # s2
            for j in range(1, m + 1):
                # s1
                A = dp[i - 1][j] and s2[i] == s3[i + j]
                B = dp[i][j - 1] and s1[j] == s3[i + j]
                dp[i][j] = A or B
        return dp[n][m]
