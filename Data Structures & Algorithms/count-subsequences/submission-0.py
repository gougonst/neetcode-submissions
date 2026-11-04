class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s = "#" + s
        t = "#" + t

        lenS, lenT = len(s), len(t)
        dp = [[0] * lenS for _ in range(lenT)]

        for i in range(1, lenS):
            if s[i] == t[1]:
                dp[1][i] = dp[1][i - 1] + 1
            else:
                dp[1][i] = dp[1][i - 1]

        for j in range(2, lenT):
            for i in range(1, lenS):
                if s[i] == t[j]:
                    dp[j][i] = dp[j - 1][i - 1] + dp[j][i - 1]
                else:
                    dp[j][i] = dp[j][i - 1]
        return dp[lenT - 1][lenS - 1]