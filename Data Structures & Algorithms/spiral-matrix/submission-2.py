class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        spiralOutput = []

        r, c = 0, 0
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                spiralOutput.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                spiralOutput.append(matrix[i][right])
            right -= 1

            if left > right or top > bottom:
                break

            for i in range(right, left - 1, -1):
                spiralOutput.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                spiralOutput.append(matrix[i][left])
            left += 1
        return spiralOutput