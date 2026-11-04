class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[M - 1][N - 1] == 1:
            return 0
        
        obstacleGrid[M - 1][N -1 ] = 1
        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if r == M - 1 and c == N - 1:
                    continue
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                    continue
                right = 0 if r + 1 == M else obstacleGrid[r + 1][c]
                down = 0 if c + 1 == N else obstacleGrid[r][c + 1]
                obstacleGrid[r][c] = right + down

        return obstacleGrid[0][0]