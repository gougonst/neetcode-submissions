class TrieNode:

    def __init__(self, alpha: str = "", isEnd: bool = False):
        self.alpha: str = alpha
        self.children: dict[str, TrieNode] = {}
        self.isEnd = isEnd


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c, False)
            node = node.children[c]
        node.isEnd = True


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        