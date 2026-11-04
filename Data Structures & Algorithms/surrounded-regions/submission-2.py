class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        notSurrounded = set()

        def dfs(r: int, c: int) -> bool:
            if r >= ROWS or r < 0 or c >= COLS or c < 0:
                return
            if (r, c) in notSurrounded:
                return
            if board[r][c] == 'X':
                return
            
            notSurrounded.add((r, c))
            for direction in DIRECTIONS:
                nr = r + direction[0]
                nc = c + direction[1]
                dfs(nr, nc)

        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in notSurrounded:
                    board[r][c] = 'X'
