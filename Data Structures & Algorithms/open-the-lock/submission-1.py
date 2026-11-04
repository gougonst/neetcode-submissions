class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque([("0000", 0)])

        visited = set(deadends)
        visited.add("0000")

        def getChildren(lock: str):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            return res

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            children = getChildren(lock)
            for child in children:
                if child in visited:
                    continue
                q.append((child, turns + 1))
                visited.add(child)
        return -1