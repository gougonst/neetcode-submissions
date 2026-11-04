class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        isSubstring = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    isSubstring[i][j] = True
                elif s[i] == s[j] and j == i + 1:
                    isSubstring[i][j] = True
                elif s[i] == s[j] and isSubstring[i + 1][j - 1]:
                    isSubstring[i][j] = True
                
                if isSubstring[i][j]:
                    count += 1

        return count