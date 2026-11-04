class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
            return memo[i]

        return max(dfs(0), dfs(1))