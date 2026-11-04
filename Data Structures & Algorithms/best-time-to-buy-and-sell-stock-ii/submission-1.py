class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # Operation:
        # 1. buy
        # 2. sell
        # 3. sell/buy
        # 4. hold
        # 5. buy/sell is meaningless
        dp = {} # (ith day, operation, hold)
        
        def dfs(i: int, hold: int, bought: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, hold, bought) in dp:
                return dp[(i, hold, bought)]

            # hold
            maxProfit = dfs(i + 1, hold, False)
            if not bought:
                # buy
                maxProfit = max(maxProfit, dfs(i + 1, prices[i], True))
            else:
                # sell
                maxProfit = max(maxProfit, prices[i] - hold + dfs(i + 1, 0, False))
                # sell then buy
                maxProfit = max(maxProfit, prices[i] - hold + dfs(i + 1, prices[i], True))
            dp[(i, hold, bought)] = maxProfit
            return dp[(i, hold, bought)]

        return dfs(0, 0, False)