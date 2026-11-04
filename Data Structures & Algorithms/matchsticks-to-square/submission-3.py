class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalLength = sum(matchsticks)
        if totalLength % 4 != 0:
            return False

        sideLength = totalLength // 4

        matchsticks.sort(reverse=True)
        visited = [False] * len(matchsticks)

        return self._dfs(matchsticks, visited, sideLength, 0, 0, 0)
        
    def _dfs(self, matchsticks: List[int], 
                   visited: List[bool], 
                   sideLength: int, 
                   cur: int, 
                   group: int, 
                   length: int) -> bool:

        if group == 4:
            return True
        if length > sideLength:
            return False
        if length == sideLength:
            return self._dfs(matchsticks, 
                             visited, 
                             sideLength, 
                             0, 
                             group + 1, 
                             0)

        for i in range(cur, len(matchsticks)):
            if visited[i]:
                continue

            visited[i] = True
            if self._dfs(matchsticks, 
                         visited, 
                         sideLength, 
                         i, 
                         group, 
                         length + matchsticks[i]):
                return True
            visited[i] = False
        return False
        