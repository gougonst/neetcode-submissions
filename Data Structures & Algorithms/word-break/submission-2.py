class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.isEnd

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # S: Length of s
        # N: Length of wordDict
        # W: Average length of word
        
        # O(NW)
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        memo = {len(s): True}

        def dfs(start: int) -> True:
            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if not trie.find(s[start:end]):
                    continue
                if dfs(end):
                    memo[start] = True
                    return True
            memo[start] = False
            return False
        
        return dfs(0)







