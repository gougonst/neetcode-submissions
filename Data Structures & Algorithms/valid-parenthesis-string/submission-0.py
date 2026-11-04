class Solution:
    def checkValidString(self, s: str) -> bool:
        maxCount, minCount = 0, 0

        for c in s:
            if c == '(':
                maxCount += 1
                minCount += 1
            elif c == ')':
                maxCount -= 1
                minCount -= 1
            else:
                maxCount += 1
                minCount -= 1

            if maxCount < 0:
                return False
            if minCount < 0:
                minCount = 0
        
        return minCount == 0










