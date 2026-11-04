class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            tmp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = tmp
        
        if a > 0x7FFFFFFF:
            return ~(a ^ mask)
        return a