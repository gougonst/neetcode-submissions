class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # "Multi-source DFS"
        rows = len(board)
        cols = len(board[0])

        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        def findWord(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True

            if r >= rows or r < 0 or c >= cols or c < 0:
                return False

            if visited[r][c]:
                return False

            if board[r][c] != word[i]:
                return False

            visited[r][c] = True
            for direction in directions:
                nr = r + direction[0]
                nc = c + direction[1]
                if findWord(nr, nc, i + 1):
                    return True
            visited[r][c] = False
            return False

        visited = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if findWord(i, j, 0):
                    return True
        return False
