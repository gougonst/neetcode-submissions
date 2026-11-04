class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        
        # Build rules:
        #   rules: {char1: [lexicographically greater then char1's chars]}
        rules = { c: set() for w in words for c in w }
        indegree = { c: 0 for c in rules.keys() }
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in rules[w1[j]]:
                        rules[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        # Topology sort
        q = collections.deque([c for c, degree in indegree.items() \
                                    if degree == 0])

        order = ""
        while q:
            c = q.popleft()
            order += c
            for neighbor in rules[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(order) != len(indegree):
            return ""
        return order