class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nRows, nCols = len(matrix), len(matrix[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = [[0] * nCols for _ in range(nRows)]

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]

            maxNeighbor = 0
            for direction in directions:
                nextR = r + direction[0]
                nextC = c + direction[1]
                if nextR >= nRows or nextR < 0 or nextC >= nCols or nextC < 0:
                    continue
                if matrix[nextR][nextC] > matrix[r][c]:
                    maxNeighbor = max(maxNeighbor, dfs(nextR, nextC))
            dp[r][c] = 1 + maxNeighbor
            return dp[r][c]

        LIP = 0
        for r in range(nRows):
            for c in range(nCols):
                LIP = max(LIP, dfs(r, c))
        return LIP