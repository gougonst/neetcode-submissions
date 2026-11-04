class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        lenW1, lenW2 = len(word1), len(word2)
        # dp: lenW2 * lenW1
        dp = [[0] * (lenW1 + 1) for _ in range(lenW2 + 1)]

        for i in range(lenW1 - 1, -1, -1):
            dp[lenW2][i] = dp[lenW2][i + 1] + 1
        for i in range(lenW2 - 1, -1, -1):
            dp[i][lenW1] = dp[i + 1][lenW1] + 1
        print(dp)

        for i in range(lenW2 - 1, -1, -1):
            for j in range(lenW1 - 1, -1, -1):
                insert = dp[i + 1][j]
                delete = dp[i][j + 1]
                replace = dp[i + 1][j + 1]
                if word1[j] != word2[i]:
                    dp[i][j] += 1 + min(insert, delete, replace)
                else:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]