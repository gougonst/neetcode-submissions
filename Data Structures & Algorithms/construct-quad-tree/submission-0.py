"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        # boudary = (top, left, bottom, right)
        boundary = (0, 0, n, n)

        def buildQuadTree(boundary: Tuple[int]) -> 'Node':
            top, left, bottom, right = boundary

            if abs(top - bottom) == 1 and abs(left - right) == 1:
                return Node(grid[top][left], True, None, None, None, None)

            centerCol, centerRow = (left + right) // 2, (top + bottom) // 2
            topLeft = buildQuadTree((top, left, centerRow, centerCol))
            topRight = buildQuadTree((top, centerCol, centerRow, right))
            bottomLeft = buildQuadTree((centerRow, left, bottom, centerCol))
            bottomRight = buildQuadTree((centerRow, centerCol, bottom, right))

            if (topLeft.isLeaf and 
                topRight.isLeaf and 
                bottomLeft.isLeaf and 
                bottomRight.isLeaf and
                topLeft.val == topRight.val and 
                topRight.val == bottomLeft.val and 
                bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True, None, None, None, None)
            else:
                return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        root = buildQuadTree(boundary)
        return root