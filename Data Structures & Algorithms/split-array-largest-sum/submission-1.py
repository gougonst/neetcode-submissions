class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp: List[List[int]] = [[-1] * k for _ in range(n)]

        def dfs(start: int, step: int) -> int:
            if start == n:
                return 0 if step == k else math.inf
            if step == k:
                return math.inf
            if dp[start][step] != -1:
                return dp[start][step]

            res = math.inf
            cur = 0
            for end in range(start, n):
                cur += nums[end]
                res = min(res, max(cur, dfs(end + 1, step + 1)))
            dp[start][step] = res
            return res

        return dfs(0, 0)
        