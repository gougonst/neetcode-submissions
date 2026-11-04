class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # Operation:
        # 1. buy
        # 2. sell
        # 3. hold
        # 4. sell/buy is meaningless
        # 5. buy/sell is meaningless
        dp = {} # (ith day, bought)
        
        # Calculate Current Profit
        def dfs(i: int, bought: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]

            # hold
            maxProfit = dfs(i + 1, bought)
            if not bought:
                # buy
                maxProfit = max(maxProfit, -prices[i] + dfs(i + 1, True))
            else:
                # sell
                maxProfit = max(maxProfit, prices[i] + dfs(i + 1, False))
            dp[(i, bought)] = maxProfit
            return dp[(i, bought)]

        return dfs(0, False)