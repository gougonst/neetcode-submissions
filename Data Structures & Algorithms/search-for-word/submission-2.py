class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i: int, r: int, c: int, visited: Set[Tuple[int, int]]) -> bool:
            if i >= len(word):
                return False
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[i]:
                return False

            if i == len(word) - 1:
                return True
            
            visited.add((r, c))
            for direction in DIRECTIONS:
                nextr, nextc = r + direction[0], c + direction[1]
                if dfs(i + 1, nextr, nextc, visited):
                    return True
            visited.remove((r, c))
            return False
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c, set()):
                    return True
        return False