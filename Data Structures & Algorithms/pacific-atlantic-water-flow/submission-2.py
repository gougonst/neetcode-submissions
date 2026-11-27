class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        toPacific = set()
        toAtlantic = set()

        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        visited = set()


        def dfs(r: int, c: int, visited: set[tuple[int, int]]) -> None:
            if (r, c) in visited:
                return
            if r == 0 or c == 0:
                toPacific.add((r, c))
            if r == rows - 1 or c == cols - 1:
                toAtlantic.add((r, c))
            
            visited.add((r, c))
            for direction in directions:
                nextr = r + direction[0]
                nextc = c + direction[1]
                if nextr >= rows or nextr < 0 or nextc >= cols or nextc < 0:
                    continue
                if heights[nextr][nextc] > heights[r][c]:
                    continue
                dfs(nextr, nextc, visited)
                if (nextr, nextc) in toAtlantic:
                    toAtlantic.add((r, c))
                if (nextr, nextc) in toPacific:
                    toPacific.add((r, c))


        res = []
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, visited)
                if (r, c) in toPacific and (r, c) in toAtlantic:
                    res.append([r, c])
        return res
