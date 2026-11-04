class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for number in range(1, n + 1):
            dp[number] = dp[number >> 1] + (number & 1)

        return dp