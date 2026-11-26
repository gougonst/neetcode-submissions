class Solution:
    def __init__(self):
        self.count = 0
        self.rows = 0
        self.cols = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == '0':
                    continue
                self.count += 1
                self.dfs(grid, r, c)
        return self.count


    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        if r >= self.rows or r < 0 or c >= self.cols or c < 0:
            return
        if grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        for direction in self.directions:
            self.dfs(
                grid, 
                r + direction[0], 
                c + direction[1]
            )