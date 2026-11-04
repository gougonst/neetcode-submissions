class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ORI_ROWS, ORI_COLS = len(matrix), len(matrix[0])
        TRANS_ROWS, TRANS_COLS = ORI_COLS, ORI_ROWS

        transMatrix = [[0] * TRANS_COLS for _ in range(TRANS_ROWS)]

        for r in range(ORI_ROWS):
            for c in range(ORI_COLS):
                transMatrix[c][r] = matrix[r][c]
        return transMatrix