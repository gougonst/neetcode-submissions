class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        # Number of stones Alice can get
        # The return value is the stones "Alice can get"
        def dfs(isAlice: bool, i: int, m: int) -> int:
            if i >= len(piles):
                return 0

            if (isAlice, i, m) in dp:
                return dp[(isAlice, i, m)]

            res = 0 if isAlice else math.inf
            # cur is number of stones that Alice / Bob can get in this round
            cur = 0
            for x in range(1, 2 * m + 1):
                if i + x - 1 >= len(piles):
                    break

                cur += piles[i + x - 1]
                if isAlice:
                    # res is number of Alice's stone
                    # Therefore, res needs to add cur
                    res = max(res, cur + dfs(not isAlice, i + x, max(m, x)))
                else:
                    # res is number of Alice's stone
                    # Therefore, res no needs to add cur
                    # cur is number of Bob's stone now
                    res = min(res, dfs(not isAlice, i + x, max(m, x)))
            dp[(isAlice, i, m)] = res
            return res

        return dfs(True, 0, 1)
