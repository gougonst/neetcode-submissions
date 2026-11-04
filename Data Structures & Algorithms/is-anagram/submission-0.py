class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount: dict[str, int] = {}
        for char in s:
            if char not in sCount:
                sCount[char] = 0
            sCount[char] += 1
        
        for char in t:
            if char not in sCount:
                return False
            sCount[char] -= 1
        
        for char, freq in sCount.items():
            if freq != 0:
                return False
        return True