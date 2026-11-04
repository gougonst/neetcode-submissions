class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found = set()

        trie = Trie()
        for word in words:
            trie.addWord(word)

        visited = set()

        def dfs(r: int, c: int, node: TrieNode, word: str):
            if r >= rows or r < 0 or c >= cols or c < 0:
                return

            if board[r][c] not in node.children:
                return

            if (r, c) in visited:
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                found.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))

        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")

        return list(found)
