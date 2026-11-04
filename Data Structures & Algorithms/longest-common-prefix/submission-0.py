class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def addWord(self, word: str):
        curNode = self._root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode.children[c].freq += 1
            curNode = curNode.children[c]

    def getRoot(self):
        return self._root


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.addWord(s)

        res = ""
        curNode = trie.getRoot()
        while len(curNode.children) == 1:
            # Only execute once
            for c in curNode.children.keys():
                freq = curNode.children[c].freq
                if freq != len(strs):
                    return res
                res += c
                curNode = curNode.children[c]
        return res
        