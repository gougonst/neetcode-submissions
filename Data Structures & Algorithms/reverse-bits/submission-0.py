class Solution:
    def reverseBits(self, n: int) -> int:
        reverseNumber = 0
        for bitCount in range(31):
            reverseNumber += n & 1
            reverseNumber <<= 1
            n >>= 1
        reverseNumber += n & 1

        return reverseNumber