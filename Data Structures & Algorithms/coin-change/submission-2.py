class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(curAmount: int) -> int:
            if curAmount == 0:
                return 0
            if curAmount in memo:
                return memo[curAmount]

            minCoins = math.inf
            for coin in coins:
                if curAmount - coin >= 0:
                    minCoins = min(minCoins, 1 + dfs(curAmount - coin))
            memo[curAmount] = minCoins
            return minCoins

        minCoins = dfs(amount)
        return minCoins if minCoins != math.inf else -1