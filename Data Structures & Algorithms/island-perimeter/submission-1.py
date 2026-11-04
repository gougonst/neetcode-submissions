DIRECTIONS = [(0, -1), (-1, 0), (1, 0), (0, 1)]

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        islandGrids = set()
        perimeter = 0

        def calcConnectedGrids(y: int, x: int) -> int:
            count = 0
            for offsetx, offsety in DIRECTIONS:
                nextx = x + offsetx
                nexty = y + offsety
                if nextx < 0 or nextx >= cols or nexty < 0 or nexty >= rows:
                    continue
                if (nexty, nextx) in islandGrids:
                    count += 1
            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    islandGrids.add((r, c))
                    connectedGrids = calcConnectedGrids(r, c)
                    perimeter += 4
                    perimeter -= 2 * connectedGrids
        return perimeter
        