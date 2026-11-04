class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def differCount(word1: str, word2: str) -> int:
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    count += 1
            return count

        def bfs(beginWord: str, endWord: str) -> int:
            count = 1
            
            q = collections.deque()
            q.append(beginWord)

            visited = set()
            
            while q:
                levelSize = len(q)
                for _ in range(levelSize):
                    word = q.popleft()
                    visited.add(word)
                    if word == endWord:
                        return count
                    for child in graph[word]:
                        if child in visited:
                            continue
                        q.append(child)
                count += 1
            return 0
        
        graph = collections.defaultdict(list)
        wordList = [beginWord] + wordList
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if differCount(wordList[i], wordList[j]) == 1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        return bfs(beginWord, endWord)
