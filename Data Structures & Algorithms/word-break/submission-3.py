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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # N: Length of s
        # M: Length of wordDict
        # T: Average length of word
        
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        memo = {len(s): True}

        def dfs(start: int) -> True:
            if start in memo:
                return memo[start]

            node = trie.root
            for i in range(start, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.isEnd:
                    if dfs(i + 1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        
        return dfs(0)







