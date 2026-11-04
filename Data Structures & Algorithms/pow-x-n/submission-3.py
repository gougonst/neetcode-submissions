class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        def dfs(x: int, n: int) -> int:
            if n <= 0:
                return 1

            val = dfs(x * x, n // 2)

            return val * x if n % 2 else val
        
        val = dfs(x, abs(n))
        
        return val if n > 0 else 1 / val

    