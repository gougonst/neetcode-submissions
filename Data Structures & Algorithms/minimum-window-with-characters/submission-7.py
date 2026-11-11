class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        tCount = Counter(t)
        remain = set(t)
        substr = (0, float("inf"))

        while r < len(s):
            while r < len(s) and remain:
                if s[r] in tCount:
                    tCount[s[r]] -= 1
                    if tCount[s[r]] <= 0:
                        remain.discard(s[r])
                r += 1
            while l < r and not remain:
                if (substr[1] == float("inf")
                    or substr[1] - substr[0] > r - l):
                    substr = (l, r)
                if s[l] in tCount:
                    tCount[s[l]] += 1
                    if tCount[s[l]] > 0:
                        remain.add(s[l])
                l += 1
        return "" if substr[1] == float("inf") else s[substr[0]:substr[1]]