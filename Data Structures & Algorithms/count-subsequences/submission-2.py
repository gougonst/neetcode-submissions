class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s = "#" + s
        t = "#" + t

        lenS, lenT = len(s), len(t)
        dp = [0] * lenS

        for i in range(1, lenS):
            dp[i] = dp[i - 1]
            if s[i] == t[1]:
                dp[i] += 1
                
        for j in range(2, lenT):
            nextDP = dp.copy()
            for i in range(1, lenS):
                nextDP[i] = nextDP[i - 1]
                if s[i] == t[j]:
                    nextDP[i] += dp[i - 1]
            dp = nextDP
        return dp[lenS - 1]