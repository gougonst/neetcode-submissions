class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        
        self._sumMatrix = [[0] * self.cols for _ in range(self.rows)]

        for r in range(self.rows - 1, -1, -1):
            for c in range(self.cols - 1, -1, -1):
                self._sumMatrix[r][c] = matrix[r][c]
                if c < self.cols - 1:
                    self._sumMatrix[r][c] += self._sumMatrix[r][c + 1]
                if r < self.rows - 1:
                    self._sumMatrix[r][c] += self._sumMatrix[r + 1][c]
                if c < self.cols - 1 and r < self.rows - 1:
                    self._sumMatrix[r][c] -= self._sumMatrix[r + 1][c + 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region = self._sumMatrix[row1][col1]
        if col2 + 1 < self.cols:
            region -= self._sumMatrix[row1][col2 + 1]
        if row2 + 1 < self.rows:
            region -= self._sumMatrix[row2 + 1][col1]
        if col2 + 1 < self.cols and row2 + 1 < self.rows:
            region += self._sumMatrix[row2 + 1][col2 + 1]
        return region
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)