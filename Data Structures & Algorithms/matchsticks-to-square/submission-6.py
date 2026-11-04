class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)
        sideLength = totalLength / 4
        if sideLength != int(sideLength):
            return False

        n = len(matchsticks)
        matchsticks.sort(reverse=True)
        used = [False] * n

        def dfs(cur: int, remain: int, grouped: int) -> bool:
            if grouped == 0:
                return True
            if remain < 0:
                return False
            if remain == 0:
                return dfs(0, sideLength, grouped - 1)

            for i in range(cur, n):
                if used[i]:
                    continue

                used[i] = True
                if dfs(i, remain - matchsticks[i], grouped):
                    return True
                used[i] = False
            return False

        return dfs(0, sideLength, 4)
        