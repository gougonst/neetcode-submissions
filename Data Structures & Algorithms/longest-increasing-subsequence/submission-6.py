class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # Ths LIS on each position (needs to include nums[i])
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                # Cannot add this, because we use the nums[j] to
                # determine whether we need to update dp[i].
                # It means dp[j] must needs to include nums[j] to
                # form the LIS.
                # else:
                #     dp[i] = max(dp[i], dp[j])
        
        return max(dp)