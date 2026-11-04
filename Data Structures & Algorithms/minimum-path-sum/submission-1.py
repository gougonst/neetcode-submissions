class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        heap = [(grid[0][0], (0, 0))]
        heapq.heapify(heap)

        visited = {(0, 0)}

        while heap:
            pathSum, (r, c) = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return pathSum
            for direction in DIRECTIONS:
                nextr, nextc = r + direction[0], c + direction[1]
                if nextr >= ROWS or nextc >= COLS:
                    continue
                if (nextr, nextc) in visited:
                    continue
                nextPathSum = pathSum + grid[nextr][nextc]
                heapq.heappush(heap, (nextPathSum, (nextr, nextc)))
                visited.add((nextr, nextc))

        return -1
                
