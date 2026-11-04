class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        toPacific = set()
        toAtlantic = set()

        pacificBoundaries = {(0, c) for c in range(COLS)} | {(r, 0) for r in range(ROWS)}
        atlanticBoundaries ={(ROWS - 1, c) for c in range(COLS)} | {(r, COLS - 1) for r in range(ROWS)}

        def dfs(r: int, c: int, prevHeight: int, visited: Set[tuple[int]]):
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return
            if prevHeight > heights[r][c]:
                return
            if (r, c) in visited:
                return

            visited.add((r, c))
            for direction in DIRECTIONS:
                nr = r + direction[0]
                nc = c + direction[1]
                dfs(nr, nc, heights[r][c], visited)

        for r, c in pacificBoundaries:
            dfs(r, c, heights[r][c], toPacific)

        for r, c in atlanticBoundaries:
            dfs(r, c, heights[r][c], toAtlantic)
        
        ans = []
        for r, c in toPacific & toAtlantic:
            ans.append([r, c])

        return ans