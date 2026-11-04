class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)
        if totalLength % 4 != 0:
            return False

        sideLength = totalLength // 4

        matchsticks.sort(reverse=True)
        visited = [False] * len(matchsticks)

        def dfs(cur, group, length) -> bool:
            if group == 3:
                return True
            if length > sideLength:
                return False
            if length == sideLength:
                return dfs(0, group + 1, 0)

            for i in range(cur, len(matchsticks)):
                if visited[i]:
                    continue

                visited[i] = True
                if dfs(i, group, length + matchsticks[i]):
                    return True
                visited[i] = False
            return False

        return dfs(0, 0, 0)
        