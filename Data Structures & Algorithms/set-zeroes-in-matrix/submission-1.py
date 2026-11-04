class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    self._updateColRow(matrix, r, c)

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0

    def _updateColRow(self, matrix: List[List[int]], r: int, c: int) -> None:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(n):
            if matrix[r][i] != 0:
                matrix[r][i] = -1
        for i in range(m):
            if matrix[i][c] != 0:
                matrix[i][c] = -1
        