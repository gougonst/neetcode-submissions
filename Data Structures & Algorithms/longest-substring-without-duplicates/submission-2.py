class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0
        chars = {}
        start = 0
        for i, c in enumerate(s):
            if c in chars and chars[c] >= start:
                start = chars[c] + 1
            chars[c] = i
            longestLen = max(longestLen, i - start + 1)
        return longestLen
