class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        maxCount = 0
        ans = 0
        l = 0

        for r, c in enumerate(s):
            count[c] += 1
            maxCount = max(maxCount, count[c])

            if r - l + 1 - maxCount > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
