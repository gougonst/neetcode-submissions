class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def updateCount(l: int, r: int) -> None:
            nonlocal count

            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            updateCount(i, i)
            updateCount(i, i + 1)

        return count