class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        DIRECTIONS = [(0, 1), (1, 0)]
        m, n = len(grid), len(grid[0])

        stack = [(grid[0][0], (0, 0))]
        visited = {(0, 0)}
        while stack:
            pathSum, (r, c) = heapq.heappop(stack)
            visited.add((r, c))
            if r == m - 1 and c == n - 1:
                return pathSum
            for offsetr, offsetc in DIRECTIONS:
                nextr, nextc = r + offsetr, c + offsetc
                if nextr >= m or nextr < 0 or nextc >= n or nextc < 0:
                    continue
                if (nextr, nextc) in visited:
                    continue
                heapq.heappush(stack, (pathSum + grid[nextr][nextc], (nextr, nextc)))
        return -1