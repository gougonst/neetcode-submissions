class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(isAlice: bool, l: int, r: int) -> int:
            if l > r:
                return 0
            if (isAlice, l, r) in dp:
                return dp[(isAlice, l, r)]

            if isAlice:
                dp[(isAlice, l, r)] = max(piles[l] + dfs(False, l + 1, r), 
                                          piles[r] + dfs(False, l, r - 1))
            else:
                dp[(isAlice, l, r)] = min(dfs(True, l + 1, r), 
                                          dfs(True, l, r - 1))
            return dp[(isAlice, l, r)]

        return dfs(True, 0, len(piles) - 1) > sum(piles) - dfs(True, 0, len(piles) - 1)