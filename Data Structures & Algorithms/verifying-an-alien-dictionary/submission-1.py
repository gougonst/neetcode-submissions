class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {}
        for charOrder, char in enumerate(order):
            orderDict[char] = charOrder

        for i in range(1, len(words)):
            prev = words[i - 1]
            cur = words[i]

            for j in range(len(prev)):
                if j >= len(cur):
                    return False
                elif orderDict[prev[j]] > orderDict[cur[j]]:
                    return False
                elif orderDict[prev[j]] < orderDict[cur[j]]:
                    break
        return True
