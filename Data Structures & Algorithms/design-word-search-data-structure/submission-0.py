class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        def searchWithDot(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.isEnd
            
            c = word[i]
            if c == '.':
                for key, child in node.children.items():
                    if searchWithDot(child, i + 1):
                        return True
                return False
            elif c not in node.children:
                return False
            else:
                return searchWithDot(node.children[c], i + 1)

        return searchWithDot(self.root, 0)
        
