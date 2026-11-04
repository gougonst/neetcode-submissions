class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        halfSum = totalSum // 2

        dp = [[False] * len(nums) for _ in range(halfSum + 1)]
        for i in range(len(nums)):
            dp[0][i] = True

        for s in range(halfSum + 1):
            for i in range(len(nums)):
                if i > 0 and dp[s][i - 1]:
                    dp[s][i] = True
                if s - nums[i] >= 0 and i > 0 and dp[s - nums[i]][i - 1]:
                    dp[s][i] = True
        return dp[halfSum][len(nums) - 1]