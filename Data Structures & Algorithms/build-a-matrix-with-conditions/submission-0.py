class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologySort(graph: Dict[int, List[int]]) -> List[int]:
            queue = deque()
            
            indegrees = { i: 0 for i in range(1, k + 1) }
            for node, neighbors in graph.items():
                for neighbor in neighbors:
                    indegrees[neighbor] += 1
            for node, count in indegrees.items():
                if count == 0:
                    queue.append(node)

            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
            return order
            

        def buildGraph(edges: List[List[int]], k: int) -> Dict[int, List[int]]:
            graph = {}
            for i in range(1, k + 1):
                graph[i] = []
            for edge in edges:
                graph[edge[0]].append(edge[1])
            return graph


        rowGraph = buildGraph(rowConditions, k)
        colGraph = buildGraph(colConditions, k)

        res = [[0] * k for _ in range(k)]

        rowOrder = topologySort(rowGraph)
        if len(rowOrder) < len(rowGraph):
            return []

        colOrder = topologySort(colGraph)
        if len(colOrder) < len(colGraph):
            return []

        rowIndexes = [0] * (k + 1)
        for i, ele in enumerate(rowOrder):
            rowIndexes[ele] = i

        colIndexes = [0] * (k + 1)
        for i, ele in enumerate(colOrder):
            colIndexes[ele] = i

        for i in range(1, k + 1):
            res[rowIndexes[i]][colIndexes[i]] = i
        
        return res
        
