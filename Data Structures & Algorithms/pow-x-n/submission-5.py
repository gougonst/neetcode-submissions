class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        res = 1
        power = abs(n)

        while power:
            # x^9 = x^b(1011) = x^b(1000) * x^b(10) * x^b(1)
            if power & 1:
                res *= x
            x *= x
            power >>= 1
        
        return res if n > 0 else 1 / res

    