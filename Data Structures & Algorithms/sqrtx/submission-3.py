class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            if m * m <= x:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans