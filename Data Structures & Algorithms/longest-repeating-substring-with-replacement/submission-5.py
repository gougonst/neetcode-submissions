class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        charCounts = {}
        maxCount = 1
        maxLen = 1
        while l <= r and r < len(s):
            charCounts[s[r]] = charCounts.get(s[r], 0) + 1
            maxCount = max(maxCount, charCounts[s[r]])
            if r - l + 1 - maxCount > k:
                charCounts[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen