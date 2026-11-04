class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        def dfs(left: int, right: int) -> int:
            if left > right:
                return 0
            if dp[left][right] != 0:
                return dp[left][right]

            for k in range(left, right + 1):
                maxSubCoin = nums[left - 1] * nums[k] * nums[right + 1]
                maxSubCoin += dfs(left, k - 1)
                maxSubCoin += dfs(k + 1, right)
                dp[left][right] = max(dp[left][right], maxSubCoin)
            return dp[left][right]


        return  dfs(1, n - 2)