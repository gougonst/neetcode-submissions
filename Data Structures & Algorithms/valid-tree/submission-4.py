class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = { i: set() for i in range(n) }
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n