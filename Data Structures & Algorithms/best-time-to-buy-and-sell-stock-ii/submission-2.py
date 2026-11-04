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