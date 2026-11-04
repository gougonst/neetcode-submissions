class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        n = len(s1)
        targetPerm = collections.Counter(s1)
        curPerm = collections.Counter(s2[:n])

        if targetPerm == curPerm:
            return True
        
        for i in range(n, len(s2)):
            oldChar = s2[i - n]
            newChar = s2[i]
            curPerm[oldChar] -= 1
            curPerm[newChar] += 1

            if targetPerm == curPerm:
                return True
        return False