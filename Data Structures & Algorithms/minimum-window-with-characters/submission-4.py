class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        tCount = Counter(t)
        remain = set(t)
        substr = ""

        while r < len(s):
            while r < len(s) and remain:
                if s[r] in tCount:
                    tCount[s[r]] -= 1
                    if tCount[s[r]] <= 0:
                        remain.discard(s[r])
                r += 1
            while l < r and not remain:
                if (substr == "" 
                    or len(substr) > (r - l)):
                    substr = s[l:r]
                if s[l] in tCount:
                    tCount[s[l]] += 1
                    if tCount[s[l]] > 0:
                        remain.add(s[l])
                l += 1
        return substr