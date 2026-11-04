class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp[amount][coin]
        dp = [[0] * n for _ in range(amount + 1)]
        for i in range(n):
            dp[0][i] = 1

        for c in range(n):
            for a in range(1, amount + 1):
                if c < 1:
                    A = 0
                else:
                    A = dp[a][c - 1]
                if a < coins[c]:
                    B = 0
                else:
                    B = dp[a - coins[c]][c]
                dp[a][c] = A + B
        return dp[amount][n - 1]