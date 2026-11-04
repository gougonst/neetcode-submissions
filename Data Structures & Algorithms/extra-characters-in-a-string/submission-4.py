class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {} # {char: TreeNode}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)

        dp = {}

        # How many character will leave at index i
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            if i in dp:
                return dp[i]

            node = trie.root
            # Need to consider both:
            # 1. Consume s[i] to form a character
            # 2. Leave s[i] is an extra character
            left = 1 + dfs(i + 1)
            for j in range(i, n):
                c = s[j]
                if c not in node.children:
                    break
                node = node.children[c]
                if node.isEnd:
                    left = min(left, dfs(j + 1))
            
            dp[i] = left
            return dp[i]

        return dfs(0)