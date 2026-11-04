class UnionFind:
    def __init__(self):
        self._roots = {}
        self._ranks = {}
        self._weights = {}

    def find(self, x) -> int:
        if x not in self._roots:
            self._roots[x] = x
            self._ranks[x] = 1
            self._weights[x] = 1

        if self._roots[x] != x:
            originRoot = self._roots[x]
            self._roots[x] = self.find(self._roots[x])
            self._weights[x] *= self._weights[originRoot]
        return self._roots[x]

    def union(self, x, y, val) -> None:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self._ranks[rootX] > self._ranks[rootY]:
                self._roots[rootY] = rootX
                self._weights[rootY] = (1 / val) * (self._weights[x] / self._weights[y])
            elif self._ranks[rootY] > self._ranks[rootX]:
                self._roots[rootX] = rootY
                self._weights[rootX] = val * (self._weights[y] / self._weights[x])
            else:
                self._roots[rootY] = rootX
                self._ranks[rootX] += 1
                self._weights[rootY] = (1 / val) * (self._weights[x] / self._weights[y])

    def getRatio(self, x, y) -> float:
        if (x not in self._roots or 
            y not in self._roots or 
            self.find(x) != self.find(y)):
            return -1
        
        return self._weights[x] / self._weights[y]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        
        for (a, b), value in zip(equations, values):
            uf.union(a, b, value)

        return [uf.getRatio(a, b) for a, b in queries]

        