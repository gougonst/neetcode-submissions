class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        wordOrder = { alphabet: i for i, alphabet in enumerate(order) }

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(len(word1)):
                if j >= len(word2):
                    return False

                if wordOrder[word1[j]] > wordOrder[word2[j]]:
                    return False
                elif wordOrder[word1[j]] < wordOrder[word2[j]]:
                    break
        return True
