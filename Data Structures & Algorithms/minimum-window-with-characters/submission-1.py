class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCount = Counter(t)
        uniqueChar = len(targetCount)

        minLength = math.inf
        ans = ""

        windowCount = {}
        satisfiedChar = 0
        start, end = 0, 0

        while end < len(s):
            windowCount[s[end]] = windowCount.get(s[end], 0) + 1
            if s[end] in targetCount and windowCount[s[end]] == targetCount[s[end]]:
                satisfiedChar += 1

            while satisfiedChar == uniqueChar:
                if end - start + 1 < minLength:
                    ans = s[start:end + 1]
                    minLength = end - start + 1
                windowCount[s[start]] -= 1
                if s[start] in targetCount and windowCount[s[start]] < targetCount[s[start]]:
                    satisfiedChar -= 1
                start += 1
            end += 1

        return ans
        


# y = X Y X W
# X W Z [Y X X W]

# [X] W Z Y X X W
# [X W] Z Y X X W
# [X W Z] Y X X W
# [X W Z Y] X X W
# [X W Z Y X] X W => candidate
# X [W Z Y X] X W
# X [W Z Y X X] W => candidate
# X W [Z Y X X] W
# X W [Z Y X X W] => candidate
# X W Z [Y X X W] => candidate
# X W Z Y [X X W]
# X W Z Y X [X W]
# X W Z Y X X [W]