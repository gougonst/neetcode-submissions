class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Calculate sum of stones
        stoneSum = sum(stones)

        # Define the expected pile's weight
        expectation = stoneSum // 2

        # Use dynamic programming based on (ith stone, current sum)
        dp = {}
        def dfs(i: int, currentSum: int) -> int:
            # The dp array should record the minimum remainnig weight
            if i >= len(stones) or currentSum >= expectation:
                return abs(currentSum - (stoneSum - currentSum))
            if (i, currentSum) in dp:
                return dp[(i, currentSum)]

            # For ith stone, we can choose to use it or not
            dp[(i, currentSum)] = min(
                dfs(i + 1, currentSum),
                dfs(i + 1, currentSum + stones[i])
            )
            return dp[(i, currentSum)]

        return dfs(0, 0)