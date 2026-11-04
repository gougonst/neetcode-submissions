class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                manhattanDistance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i].append((j, manhattanDistance))
                graph[j].append((i, manhattanDistance))

        visited = set()
        minHeap = [(0, 0)]
        cost = 0
        while minHeap:
            distance, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            cost += distance
            visited.add(point)
            for neighbor, distance in graph[point]:
                heapq.heappush(minHeap, (distance, neighbor))
        return cost