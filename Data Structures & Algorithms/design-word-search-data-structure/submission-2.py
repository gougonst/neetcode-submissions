class TrieNode:

    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True
        

    def search(self, word: str) -> bool:

        def searchFromNode(node: TrieNode, i: int) -> bool:
            if i >= len(word):
                return node.isEnd
            
            c = word[i]
            if c != '.':
                if c not in node.children:
                    return False
                return searchFromNode(node.children[c], i + 1)
            
            for child in node.children.values():
                if searchFromNode(child, i + 1):
                    return True
            return False
        
        return searchFromNode(self.root, 0)
        
