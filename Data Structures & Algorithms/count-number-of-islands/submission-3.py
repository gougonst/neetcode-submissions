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
                self.bfs(grid, r, c)
        return self.count


    def bfs(self, grid: List[List[str]], r: int, c: int) -> None:
        q = deque()
        q.append((r, c))
        while q:
            qLen = len(q)
            for _ in range(qLen):
                land = q.popleft()
                for direction in self.directions:
                    nextr = land[0] + direction[0]
                    nextc = land[1] + direction[1]
                    if nextr >= self.rows or nextr < 0 or nextc >= self.cols or nextc < 0:
                        continue
                    if grid[nextr][nextc] == '1':
                        q.append((nextr, nextc))
                        grid[nextr][nextc] = '0'






        