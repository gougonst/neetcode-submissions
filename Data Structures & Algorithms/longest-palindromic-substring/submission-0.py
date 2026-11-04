class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxIdx = 0
        maxLen = 0

        def updateMaxPalindrome(l, r) -> str:
            nonlocal maxIdx, maxLen

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxIdx = l
                    maxLen = r - l + 1
                r += 1
                l -= 1

        for i in range(n):
            updateMaxPalindrome(i, i)
            updateMaxPalindrome(i, i + 1)

        return s[maxIdx:maxIdx + maxLen]
