class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False


class Solution:

    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.trie = TrieNode()
        self.board = None
        self.res = set()


    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for word in words:
            self.addWord(word)

        for r in range(self.rows):
            for c in range(self.cols):
                self.dfs(r, c, self.trie, set(), "")

        return list(self.res)

    
    def dfs(self, r: int, c: int, node: TrieNode, visited: set[tuple[int, int]], word: str) -> None:
        if r >= self.rows or r < 0 or c >= self.cols or c < 0:
            return
        if (r, c) in visited:
            return
        if self.board[r][c] not in node.children:
            return

        word += self.board[r][c]
        visited.add((r, c))

        if node.children[self.board[r][c]].isEnd:
            self.res.add(word)

        for direction in self.directions:
            self.dfs(
                r + direction[0], 
                c + direction[1], 
                node.children[self.board[r][c]], 
                visited, 
                word
            )

        visited.remove((r, c))
        word = word[:-1]

        