class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = { i: [] for i in range(n) }
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()

        def dfs(node: int, parent: int) -> None:
            if node in visited:
                return

            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count
