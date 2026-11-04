class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permCount = {}
        for c in s1:
            permCount[c] = permCount.get(c, 0) + 1
        
        start, end = 0, 0

        for start in range(len(s2)):
            if s2[start] not in permCount:
                continue
            end = max(end, start)
            while end < len(s2) and s2[end] in permCount and permCount[s2[end]] > 0:
                permCount[s2[end]] -= 1
                end += 1
            if end - start == len(s1):
                return True
            permCount[s2[start]] += 1
        return False