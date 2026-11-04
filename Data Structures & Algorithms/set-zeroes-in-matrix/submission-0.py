class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        updateCols, updateRows = set(), set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    updateCols.add(c)
                    updateRows.add(r)

        for r in updateRows:
            for c in range(n):
                matrix[r][c] = 0
        for c in updateCols:
            for r in range(m):
                matrix[r][c] = 0
        