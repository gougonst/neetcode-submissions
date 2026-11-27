class TrieNode:

    def __init__(self):
        self.children = {}
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
        def dfs(i: int, node: TrieNode) -> bool:
            if i == len(word):
                return node.isEnd

            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                return dfs(i + 1, node.children[word[i]])
            
            for child in node.children.values():
                if dfs(i + 1, child):
                    return True
            return False

        return dfs(0, self.root)

    
    

        
