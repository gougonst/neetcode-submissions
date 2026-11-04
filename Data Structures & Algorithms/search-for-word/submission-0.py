class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # "Multi-source DFS"
        # Find the first character in the board first to form multi-source.
        r = len(board)
        c = len(board[0])
        sources = []
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    sources.append([i, j])

        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        def findWord(pos: List[int], visited: List[List[bool]], i: int) -> bool:
            if i >= len(word):
                return True

            target = word[i]
            for direction in directions:
                nr = pos[0] + direction[0]
                nc = pos[1] + direction[1]
                if nr >= r or nr < 0 or nc >= c or nc < 0:
                    continue
                if visited[nr][nc]:
                    continue
                if board[nr][nc] != target:
                    continue
                visited[nr][nc] = True
                if findWord([nr, nc], visited, i + 1):
                    return True
                visited[nr][nc] = False
            return False

        # For each source, use DFS to find whether word exists.
        for source in sources:
            visited = [[False] * c for _ in range(r)]
            visited[source[0]][source[1]] = True
            if findWord(source, visited, 1):
                return True
        return False
