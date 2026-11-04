class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[M - 1][N - 1] == 1:
            return 0
        
        pathCount = {}

        # At point (x, y), how many paths can get to (M-1, N-1)
        def dfs(x: int, y: int) -> int:
            if x >= N or y >= M:
                return 0
            if obstacleGrid[y][x] == 1:
                return 0
            if y == M - 1 and x == N - 1:
                return 1
            if (x, y) in pathCount:
                return pathCount[(x, y)]
            
            paths = dfs(x + 1, y) + dfs(x, y + 1)
            pathCount[(x, y)] = paths
            return paths

        return dfs(0, 0)