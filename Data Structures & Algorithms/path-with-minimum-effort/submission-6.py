class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        visited = [[False] * COLS for _ in range(ROWS)]
        minimumEffort = 0

        minHeap = [(0, (0, 0))]
        while minHeap:
            cur = heapq.heappop(minHeap)
            effort, r, c = cur[0], cur[1][0], cur[1][1]
            minimumEffort = max(minimumEffort, effort)
            visited[r][c] = True
            if r == ROWS - 1 and c == COLS - 1:
                break
            for direction in DIRECTIONS:
                nextr = r + direction[0]
                nextc = c + direction[1]
                if nextr >= ROWS or nextr < 0 or nextc >= COLS or nextc < 0:
                    continue
                if visited[nextr][nextc]:
                    continue
                nextEffort = abs(heights[r][c] - heights[nextr][nextc])
                heapq.heappush(minHeap, (nextEffort, (nextr, nextc)))

        return minimumEffort
