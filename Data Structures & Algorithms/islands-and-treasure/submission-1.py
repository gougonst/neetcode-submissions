class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INIT_LAND = pow(2, 31) - 1
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r: int, c: int) -> None:
            visited = [[False] * COLS for _ in range(ROWS)]
            q = collections.deque()
            for direction in DIRECTIONS:
                q.append((r + direction[0], c + direction[1]))
            step = 0
            while q:
                levelSize = len(q)
                step += 1
                for _ in range(levelSize):
                    r, c = q.popleft()
                    if r >= ROWS or r < 0 or c >= COLS or c < 0:
                        continue
                    if grid[r][c] == -1 or grid[r][c] == 0:
                        continue
                    if visited[r][c]:
                        continue
                    visited[r][c] = True
                    grid[r][c] = min(grid[r][c], step)
                    for direction in DIRECTIONS:
                        q.append((r + direction[0], c + direction[1]))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)