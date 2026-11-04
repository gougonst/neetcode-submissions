class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(isAlice: bool, i: int, m: int) -> int:
            if i >= len(piles):
                return 0

            if (isAlice, i, m) in dp:
                return dp[(isAlice, i, m)]

            res = 0 if isAlice else math.inf
            cur = 0
            for x in range(1, 2 * m + 1):
                if i + x - 1 >= len(piles):
                    break

                cur += piles[i + x - 1]
                if isAlice:
                    res = max(res, cur + dfs(not isAlice, i + x, max(m, x)))
                else:
                    res = min(res, dfs(not isAlice, i + x, max(m, x)))
            dp[(isAlice, i, m)] = res
            return res

        return dfs(True, 0, 1)