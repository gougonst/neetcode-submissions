class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def dfs(i, end, memo):
            if i >= end:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1, end, memo), nums[i] + dfs(i + 2, end, memo))
            return memo[i]

        return max(dfs(0, n - 1, [-1] * n), dfs(1, n, [-1] * n))
        