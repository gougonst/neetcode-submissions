class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[None] * n for _ in range(n)]

        def dfs(i, openBrackets) -> bool:
            if i >= n or openBrackets >= n:
                return openBrackets == 0
            if openBrackets < 0:
                return False
            if dp[i][openBrackets] is not None:
                return dp[i][openBrackets]
            
            if s[i] == '(':
                res = dfs(i + 1, openBrackets + 1)
            elif s[i] == ')':
                res = dfs(i + 1, openBrackets - 1)
            else:
                res = (dfs(i + 1, openBrackets) or 
                       dfs(i + 1, openBrackets + 1) or 
                       dfs(i + 1, openBrackets - 1))
            dp[i][openBrackets] = res
            return dp[i][openBrackets]

        return dfs(0, 0)










