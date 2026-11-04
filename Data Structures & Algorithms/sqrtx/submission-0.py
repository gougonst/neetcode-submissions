class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        prev, next = 1, 1
        while next * next <= x:
            prev = next
            next += 1
        return prev