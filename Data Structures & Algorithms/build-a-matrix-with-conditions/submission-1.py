class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologySort(edges: List[List[int]]) -> List[int]:
            # Build graph and indegrees
            graph = [[] for _ in range(k + 1)]
            indegrees = [0] * (k + 1)

            for u, v in edges:
                graph[u].append(v)
                indegrees[v] += 1

            # Topology sort
            queue = deque([i for i in range(1, k + 1) if indegrees[i] == 0])

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
            return order


        rowOrder = topologySort(rowConditions)
        if len(rowOrder) < k:
            return []

        colOrder = topologySort(colConditions)
        if len(colOrder) < k:
            return []

        res = [[0] * k for _ in range(k)]

        rowIndexes = [0] * (k + 1)
        for i, ele in enumerate(rowOrder):
            rowIndexes[ele] = i

        colIndexes = [0] * (k + 1)
        for i, ele in enumerate(colOrder):
            colIndexes[ele] = i

        for i in range(1, k + 1):
            res[rowIndexes[i]][colIndexes[i]] = i
        
        return res
        
