class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        ans = x
        for _ in range(abs(n) - 1):
            ans *= x
        
        if n < 0:
            return 1 / ans
        else:
            return ans