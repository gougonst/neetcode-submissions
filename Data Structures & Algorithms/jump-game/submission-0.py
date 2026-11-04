class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 1

        def dfs(start: int) -> bool:
            if start >= n:
                return False
            if dp[start] != -1:
                return bool(dp[start])

            maxJumpLength = nums[start]
            for jumpLength in range(1, maxJumpLength + 1):
                if dfs(start + jumpLength):
                    dp[start] = 1
                    break
            if dp[start] == -1:
                dp[start] = 0

            return bool(dp[start])

        return dfs(0)
        

# X X X i X
# dp[i] = Whether it can jump to last index
# State:
#     1: Yes, it can
#     0: No, it can't
#     -1: Not determined yet.
# for each i, jump to every position that it can jump to.