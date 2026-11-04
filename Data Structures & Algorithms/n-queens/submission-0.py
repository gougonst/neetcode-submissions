class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        solution = [["."] * n for _ in range(n)]
        cols = set()
        negDiags = set()
        posDiags = set()

        def dfs(r: int) -> None:
            # End criteria:
            # 1. i >= n, add solution
            # 2. i < n and no availables, invalid
            if r >= n:
                copy = ["".join(row) for row in solution]
                solutions.append(copy)
                return

            # Select each available position, dfs with i + 1
            for c in range(n):
                if c in cols or (r + c) in posDiags or (r - c) in negDiags:
                    continue
                
                cols.add(c)
                posDiags.add(r + c)
                negDiags.add(r - c)
                solution[r][c] = "Q"

                dfs(r + 1)

                cols.remove(c)
                posDiags.remove(r + c)
                negDiags.remove(r - c)
                solution[r][c] = "."

        dfs(0)
        return solutions