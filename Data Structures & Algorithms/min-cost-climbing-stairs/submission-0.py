class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        totalCosts = [0] * (n)
        totalCosts[0] = cost[0]
        totalCosts[1] = cost[1]
        for i in range(2, n):
            totalCosts[i] = cost[i] + min(totalCosts[i - 1], totalCosts[i - 2])
        return min(totalCosts[n - 1], totalCosts[n - 2])