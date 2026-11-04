class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCount = Counter(t)
        distinct = set(t)
        satisfied = set()
        start, end = 0, 0
        minLength = math.inf
        ans = ""

        while end < len(s):
            targetCount[s[end]] -= 1
            if s[end] in distinct and targetCount[s[end]] <= 0:
                satisfied.add(s[end])

            while len(satisfied) == len(distinct):
                if end - start + 1 < minLength:
                    ans = s[start:end + 1]
                    minLength = end - start + 1
                targetCount[s[start]] += 1
                if s[start] in distinct and targetCount[s[start]] > 0:
                    satisfied.remove(s[start])
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