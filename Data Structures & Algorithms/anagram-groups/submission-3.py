class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramLists: Dict[Tuple[int], List[str]] = {}

        for s in strs:
            freq = self.getStringFreq(s)
            if freq not in anagramLists:
                anagramLists[freq] = []
            anagramLists[freq].append(s)

        ans: List[List[str]] = []
        for anagrams in anagramLists.values():
            ans.append(anagrams)
        return ans

        
    def getStringFreq(self, s: str) -> Tuple[int]:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        return tuple(freq)