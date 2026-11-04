class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(heights), len(heights[0])

        visited = set()

        candidates = [(0, 0, 0)] # List[Tuple[int, int, int]], [(effort, y, x)]

        while candidates:
            effort, y, x = heapq.heappop(candidates)
            if (y, x) in visited:
                continue
            visited.add((y, x))
            if y == ROWS - 1 and x == COLS - 1:
                return effort
            for yOffset, xOffset in DIRECTIONS:
                newy, newx = y + yOffset, x + xOffset
                if newy < 0 or newy >= ROWS or newx < 0 or newx >= COLS:
                    continue
                if (newy, newx) in visited:
                    continue
                newEffort = max(effort, abs(heights[newy][newx] - heights[y][x]))
                heapq.heappush(candidates, (newEffort, newy, newx))
        return -1