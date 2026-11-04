class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndexes = {}
        startIndex = 0

        longestLength = 0
        for i, c in enumerate(s):
            if c in lastIndexes and lastIndexes[c] >= startIndex:
                startIndex = lastIndexes[c] + 1
            lastIndexes[c] = i

            longestLength = max(longestLength, i - startIndex + 1)
        return longestLength