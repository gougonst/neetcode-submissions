class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            combs = 0
            for num in nums:
                if i - num < 0:
                    continue
                combs += dp[i - num]
            dp[i] = combs
        return dp[target]