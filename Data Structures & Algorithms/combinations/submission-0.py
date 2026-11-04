class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(cur: List[int], i: int, depth: int):
            if depth == k:
                res.append(cur.copy())

            for j in range(i, n + 1):
                cur.append(j)
                dfs(cur, j + 1, depth + 1)
                cur.pop()

        dfs([], 1, 0)
        return res