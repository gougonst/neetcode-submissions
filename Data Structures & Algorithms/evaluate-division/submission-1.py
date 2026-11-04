class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i in range(len(equations)):
            A = equations[i][0]
            B = equations[i][1]
            val = values[i]
            graph[A].append((B, val))
            graph[B].append((A, 1 / val))
        
        def dfs(node: str, val: float, target: str) -> int:
            if node not in graph:
                return -1
            if node in visited:
                return -1
            if node == target:
                return val
            
            visited.add(node)

            for neighbor, weight in graph[node]:
                res = dfs(neighbor, val * weight, target)
                if res != -1:
                    return res

            visited.remove(node)
            return -1

        ans = []
        for query in queries:
            visited = set()
            ans.append(dfs(query[0], 1, query[1]))

        return ans