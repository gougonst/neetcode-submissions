class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children.keys():
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True


    def search(self, word: str) -> bool:
        lastNode = self._getLastNode(word)
        if lastNode is None:
            return False
        return lastNode.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        lastNode = self._getLastNode(prefix)
        return lastNode is not None

    def _getLastNode(self, word) -> TrieNode:
        node = self.root
        for c in word:
            if c not in node.children.keys():
                return None
            node = node.children[c]
        return node
        