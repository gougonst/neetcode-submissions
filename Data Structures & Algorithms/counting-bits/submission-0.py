class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        dp[0] = 0

        for number in range(1, n + 1):
            firstPart = number & (number - 1)
            secondPart = number - firstPart

            if firstPart == 0:
                dp[number] = 1
            else:
                dp[number] = dp[firstPart] + dp[secondPart]

        return dp