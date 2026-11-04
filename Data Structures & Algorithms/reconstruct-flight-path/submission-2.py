class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = collections.defaultdict(collections.deque)
        for src, dest in tickets:
            graph[src].append(dest)

        path = collections.deque()

        def dfs(airport: str):
            while graph[airport]:
                nextAirport = graph[airport].popleft()
                dfs(nextAirport)

            path.appendleft(airport)

        dfs("JFK")
        return list(path)