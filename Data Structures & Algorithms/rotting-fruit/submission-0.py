class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = collections.deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        visited = [[False] * COLS for _ in range(ROWS)]
        minutes = 0
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                r, c = q.popleft()
                for direction in DIRECTIONS:
                    nr = r + direction[0]
                    nc = c + direction[1]
                    if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0:
                        continue
                    if grid[nr][nc] != 1:
                        continue
                    if visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc))
            if q:
                minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and not visited[r][c]:
                    return -1
        return minutes