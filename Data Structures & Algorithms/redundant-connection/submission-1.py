class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n + 1)]
        self.ranks = [0 for _ in range(n + 1)]

    def find(self, node: int) -> int:
        if node != self.roots[node]:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]

    # Union & Determine whether the same connected component
    def union(self, x: int, y: int) -> bool:
        rootx, rooty = self.find(x), self.find(y)
        
        # Same connected component
        if rootx == rooty:
            return True

        # Different connected component
        if self.ranks[rootx] == self.ranks[rooty]:
            self.roots[rootx] = rooty
            self.ranks[rooty] += 1
        elif self.ranks[rootx] < self.ranks[rooty]:
            self.roots[rootx] = rooty
        else:
            self.roots[rooty] = rootx
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))
        for edge in edges:
            if unionFind.union(edge[0], edge[1]):
                return edge
        return []
