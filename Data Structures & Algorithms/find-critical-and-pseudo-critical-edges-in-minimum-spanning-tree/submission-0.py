class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.roots = [i for i in range(n)]
        self.ranks = [1] * n

    def find(self, x: int) -> int:
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x: int, y: int) -> bool:
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot == yRoot:
            return False

        self.n -= 1

        if self.ranks[xRoot] > self.ranks[yRoot]:
            self.roots[yRoot] = xRoot
        elif self.ranks[xRoot] < self.ranks[yRoot]:
            self.roots[xRoot] = yRoot
        else:
            self.roots[yRoot] = xRoot
            self.ranks[xRoot] += 1
        return True

    def isConnected(self) -> bool:
        return self.n == 1


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        critical, pseudo = [], []

        for i, edge in enumerate(edges):
            edge.append(i) # [v1, v2, weight, original_index]
        edges.sort(key=lambda x: x[2])

        # Global MST
        uf = UnionFind(n)
        mstWeight = 0
        for v1, v2, weight, i in edges:
            if uf.union(v1, v2):
                mstWeight += weight

        for v1, v2, w, i in edges:
            # Find critical edges
            uf = UnionFind(n)
            weight = 0
            for n1, n2, edgeWeight, j in edges:
                # Skip current iterate edge to see if it is critical or not
                if i == j:
                    continue
                if uf.union(n1, n2):
                    weight += edgeWeight
            if not uf.isConnected() or weight > mstWeight:
                critical.append(i)
                continue

            # Find pseudo critical edges
            uf = UnionFind(n)   
            # Force use current iterate edge to see if it is pseudo or not
            # If a edge can form a MST and it is not a critical edge, than it is a 
            #   pseudo critical edge
            uf.union(v1, v2)
            weight = w
            for n1, n2, edgeWeight, j in edges:
                if uf.union(n1, n2):
                    weight += edgeWeight
            if weight == mstWeight:
                pseudo.append(i)
        
        return [critical, pseudo]