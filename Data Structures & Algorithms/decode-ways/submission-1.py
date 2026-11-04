class Solution:
    def numDecodings(self, s: str) -> int:
        # count: int
        # Crete a mapping table
        # DFS Algorithm:
        # Prefix: Fixed in current state.
        # i: Current index
        # End criteria: i > len(s)
        # For each character in s, I can choose whether use it or not
        #   If choose use i ~ j, it is invalid, return ""
        #   If it is valid, count + 1
        #     Do next dfs
        #   If not choose use i ~ j, keep track i ~ j + 1
        memo = [-1] * len(s)

        def dfs(start: int) -> int:
            if start == len(s):
                return 1
            if s[start] == "0":
                return 0
            if memo[start] != -1:
                return memo[start]

            res = 0
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if int(substr) < 1 or int(substr) > 26:
                    break
                res += dfs(end)
            memo[start] = res
            return res

        return dfs(0)