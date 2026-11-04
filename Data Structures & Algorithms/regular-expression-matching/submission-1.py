class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        s = '#' + s
        p = '#' + p
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = p[j] == '*' and dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j].isalpha():
                    dp[i][j] = (s[i] == p[j]) and dp[i - 1][j - 1]
                elif p[j] == '*':
                    condition1 = p[j - 1] == '.' and dp[i - 1][j]
                    condition2 = (s[i] == p[j - 1]) and dp[i - 1][j]
                    condition3 = dp[i][j - 2]
                    dp[i][j] = condition1 or condition2 or condition3
                else:
                    pass
                    # TODO: Error handling
        return dp[m][n]



# s: X X X X W,   index: i, len: m
# p: Y Y Z *,     index: j, len: n

# p[j] == '.'
# dp[i - 1][j - 1]

# p[j] == alphabet
# (s[i] == p[j]) and dp[i - 1][j - 1]

# p[j] == '*'
# p[j - 1] == '.': dp[i - 1][j]
# (s[i] == p[j - 1]) and (s[i] == alphabet): dp[i - 1][j]
# (s[i] == alphabet): dp[i][j - 2]

# s: ,   index: i, len: m
# p: Y * Y *,     index: j, len: n
# dp[0][j]: p[j] == '*' and dp[0][j - 2]

# s: X X X X X,   index: i, len: m
# p: ,     index: j, len: n
# dp[i][0]: False

# s: ,   index: i, len: m
# p: ,     index: j, len: n
# dp[0][0]: True

