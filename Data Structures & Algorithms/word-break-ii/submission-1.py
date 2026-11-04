class TrieNode:
    def __init__(self):
        self.children = defaultdict(str)
        self.isEnd = False


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
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Build Trie
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)

        # Build index words
        indexWords = defaultdict(list)

        def buildIndexWords(start: int) -> None:
            if start >= len(s):
                return
            if s[start] not in trie.root.children:
                return
            if start in indexWords:
                return
            
            node = trie.root
            cur = ""
            for i in range(start, len(s)):
                if s[i] not in node.children:
                    break
                cur += s[i]
                if node.children[s[i]].isEnd:
                    indexWords[start].append(cur)
                    buildIndexWords(i + 1)
                node = node.children[s[i]]

        buildIndexWords(0)

        # Build word break
        memo = {}

        def buildWordBreak(start: int) -> List[str]:
            if start == len(s):
                return [""]
            if start not in indexWords:
                return []
            if start in memo:
                return memo[start]
            
            combs = []
            for word in indexWords[start]:
                children = buildWordBreak(start + len(word))
                if not children:
                    continue
                for child in children:
                    combs.append(f"{word} {child}".strip())
            memo[start] = combs
            return combs

        return buildWordBreak(0)