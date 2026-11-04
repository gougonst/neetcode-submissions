class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = 0
        usedCol = set()
        usedPosDiag = set()
        usedNegDiag = set()

        def dfs(r: int) -> None:
            nonlocal solutions
            if r == n:
                solutions += 1
                return

            for c in range(n):
                if (c in usedCol or 
                    r + c in usedPosDiag or 
                    r - c in usedNegDiag):
                    continue
                usedCol.add(c)
                usedPosDiag.add(r + c)
                usedNegDiag.add(r - c)
                dfs(r + 1)
                usedCol.remove(c)
                usedPosDiag.remove(r + c)
                usedNegDiag.remove(r - c)

        dfs(0)
        return solutions
            