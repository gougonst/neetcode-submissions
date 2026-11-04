class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> None:
            if r >= rows or r < 0 or c >= cols or c < 0:
                return
            if grid[r][c] == "0":
                return
            if visited[r][c]:
                return

            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse each cell
        count = 0
        for r in range(rows):
            for c in range(cols):
                # Assign visited cell to 1 to represent visited
                if grid[r][c] == "0" or visited[r][c]:
                    continue
                
                dfs(r, c)
                count += 1
        return count