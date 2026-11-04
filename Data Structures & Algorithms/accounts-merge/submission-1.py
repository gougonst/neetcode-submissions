class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        emailToName = {}

        for account in accounts:
            name = account[0]
            root = account[1]
            emailToName[root] = name
            for email in account[2:]:
                graph[root].append(email)
                graph[email].append(root)

        visited = set()

        def dfs(email: str, cur: List[str]) -> List[str]:
            if email in visited:
                return cur

            visited.add(email)
            cur.append(email)
            for neighbor in graph[email]:
                dfs(neighbor, cur)
            return cur

        res = []
        for email, name in emailToName.items():
            if email in visited:
                continue
            res.append([name] + sorted(dfs(email, [])))
        return res