class Solution:
    def minEnd(self, n: int, x: int) -> int:
        xBits = []
        while x > 0:
            xBits.append(x % 2)
            x >>= 1

        n = n - 1
        nBits = []
        while n > 0:
            nBits.append(n % 2)
            n >>= 1

        j = 0
        for nBit in nBits:
            while j < len(xBits) and xBits[j] == 1:
                j += 1

            if j == len(xBits):
                xBits.append(0)
            
            xBits[j] = nBit
            j += 1
        
        ans = 0
        for xBit in reversed(xBits):
            ans += xBit
            ans <<= 1
        ans >>= 1
        return ans