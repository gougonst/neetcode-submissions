class Solution:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.dfs(board, word, set(), r, c, 0):
                    return True
        return False


    def dfs(self, board: List[List[str]], word: str, visited: set[tuple[int, int]], r: int, c: int, i: int) -> bool:
        if r >= self.rows or r < 0 or c >= self.cols or c < 0:
            return False
        if i >= len(word):
            return False
        if (r, c) in visited:
            return False
        if word[i] != board[r][c]:
            return False
        if i == len(word) - 1:
            return True

        visited.add((r, c))
        for direction in self.directions:
            if self.dfs(
                board, 
                word, 
                visited, 
                r + direction[0], 
                c + direction[1], 
                i + 1
            ):
                return True
        visited.remove((r, c))

        return False

        