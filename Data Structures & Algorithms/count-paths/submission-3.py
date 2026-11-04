class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1] * n

        for _ in range(m - 1):
            newMemo = memo.copy()
            for j in range(n - 2, -1, -1):
                newMemo[j] = newMemo[j + 1] + memo[j]
            memo = newMemo
        return memo[0]