class Solution:
    def minEnd(self, n: int, x: int) -> int:
        xBits  = []
        zeroBits = 0
        while x > 0:
            xBits.append(x & 1)
            if x & 1 == 0:
                zeroBits += 1
            x >>= 1
        
        additionBits = math.ceil(n ** 0.5) - zeroBits
        ansBits = xBits + [0] * additionBits

        nBits = []
        n -= 1
        while n > 0:
            nBits.append(n & 1)
            n >>= 1

        nIdx = 0
        for i in range(len(ansBits)):
            if ansBits[i] == 0:
                ansBits[i] = nBits[nIdx]
                nIdx += 1
            if nIdx >= len(nBits):
                break
            
        ans = 0
        for bit in reversed(ansBits):
            ans = (ans << 1) | bit
        return ans        