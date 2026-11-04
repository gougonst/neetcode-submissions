class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)

        gcdLen = gcd(len(str1), len(str2))
        return str1[:gcdLen]