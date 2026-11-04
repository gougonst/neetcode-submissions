class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        totalCosts = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if totalCosts[i] != -1:
                return totalCosts[i]
            return cost[i] + min(dfs(i - 1), dfs(i - 2))

        return min(dfs(n - 1), dfs(n - 2))