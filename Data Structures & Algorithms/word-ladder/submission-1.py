class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
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
                    neighbors = set()
                    for i in range(wordLen):
                        neighbors.update(graph[word[:i] + "*" + word[i + 1:]])
                    for neighbor in neighbors:
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                count += 1
            return 0
        
        wordLen = len(beginWord)
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                graph[word[:i] + "*" + word[i + 1:]].append(word)

        return bfs(beginWord, endWord)
