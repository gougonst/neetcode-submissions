class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLen = 0
        chars = set()
        start = 0
        for i, c in enumerate(s):
            if c not in chars:
                chars.add(c)
                longestLen = max(longestLen, i - start + 1)
                continue
            while s[start] != c:
                chars.remove(s[start])
                start += 1
            start += 1
        return longestLen
