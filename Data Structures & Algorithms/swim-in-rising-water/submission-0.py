class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Algorithm: BFS
        # Data Structure: Maintain a priority queue, (height, (r, c))
        #                 Maintain a time (int)
        # 1. Push top-left to queue
        # 2. Pop element from queue
        # 3. Mark grid as visited
        # 4. Update time with the height
        # 5. Push the adjacent grids to queue
        # 6. Back to 2.
        ROWS = len(grid)
        COLS = len(grid[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        minHeap = []
        heapq.heappush(minHeap, (grid[0][0], (0, 0)))

        visited = set((0, 0))

        time = 0
        while minHeap[0][1] != (ROWS - 1, COLS - 1):
            # BFS
            height, (r, c) = heapq.heappop(minHeap)
            visited.add((r, c))
            time = max(time, height)
            for direction in DIRECTIONS:
                nr = r + direction[0]
                nc = c + direction[1]
                if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0:
                    continue
                if (nr, nc) in visited:
                    continue
                heapq.heappush(minHeap, (grid[nr][nc], (nr, nc)))
                
        return max(time, minHeap[0][0])