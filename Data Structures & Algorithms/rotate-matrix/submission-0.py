class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n):
            for c in range(r, n - r - 1):
                temp = matrix[r][c]
                matrix[r][c] = matrix[n - 1 - c][r]
                matrix[n - 1 - c][r] = matrix[n - 1 - r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[c][n - 1 - r]
                matrix[c][n - 1 - r] = temp