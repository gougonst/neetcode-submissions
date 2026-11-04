class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.roots = [i for i in range(n)]
        self.ranks = [0] * n

    def find(self, x: int) -> int:
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x: int, y: int) -> None:
        xRoot, yRoot = self.find(x), self.find(y)

        if xRoot == yRoot:
            return

        if self.ranks[xRoot] > self.ranks[yRoot]:
            self.roots[yRoot] = xRoot
        elif self.ranks[xRoot] < self.ranks[yRoot]:
            self.roots[xRoot] = yRoot
        else:
            self.roots[yRoot] = xRoot
            self.ranks[xRoot] += 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)

        n = len(nums)

        # Build graph
        graph = defaultdict(set)
        for i in range(n):
            for j in range(i, n):
                if gcd(nums[i], nums[j]) != 1:
                    graph[i].add(j)
                    graph[j].add(i)

        # Check connected component
        unionFind = UnionFind(n)
        for node, edges in graph.items():
            for edge in edges:
                unionFind.union(node, edge)
        root = unionFind.find(0)
        for i in range(1, n):
            if unionFind.find(i) != root:
                return False
        return True