class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for src, dest, time in times:
            graph[src].append((dest, time))

        minHeap = [(0, k)]
        visited = set()
        minDelay = 0

        while minHeap:
            delay, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            minDelay = max(minDelay, delay)
            for dest, time in graph[node]:
                if dest not in visited:
                    heapq.heappush(minHeap, (delay + time, dest))

        return minDelay if len(visited) == n else -1