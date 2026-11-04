class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if r >= rows or r < 0 or c >= cols or c < 0:
                return 0
            if visited[r][c] or grid[r][c] == 0:
                return 0

            area = 0
            visited[r][c] = True
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                area += dfs(nr, nc)
            return area + 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or visited[r][c]:
                    continue
                area = dfs(r, c)
                maxArea = max(maxArea, area)
        return maxArea