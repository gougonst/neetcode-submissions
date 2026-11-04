class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        xMsb, nMsb = 1, 1

        # if n = 4, [0, 0], [0, 1], [1, 0], [1, 1] => which the biggest one is 3
        while nMsb <= n - 1:
            if xMsb & x == 0:
                if nMsb & (n - 1):
                    res |= xMsb
                nMsb <<= 1
            xMsb <<= 1
        return res