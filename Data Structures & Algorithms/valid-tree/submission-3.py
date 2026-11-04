class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = { i: set() for i in range(n) }
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False

            visited.add(node)
            for child in graph[node]:
                if child == node:
                    return False
                graph[child].remove(node)
                if not dfs(child):
                    return False
            return True

        result = dfs(0)
        return len(visited) == n and result