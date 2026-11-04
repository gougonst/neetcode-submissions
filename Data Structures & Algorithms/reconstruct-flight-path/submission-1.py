class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = collections.defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        path = ["JFK"]

        def dfs(airport: str) -> bool:
            if len(path) == len(tickets) + 1:
                return True
            if not graph[airport]:
                return False

            temp = list(graph[airport])
            for i, neighbor in enumerate(temp):
                graph[airport].pop(i)
                path.append(neighbor)

                if dfs(neighbor):
                    return True
                
                graph[airport].insert(i, neighbor)
                path.pop()
            return False

        dfs("JFK")
        return path