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

        self.n -= 1

        if self.ranks[xRoot] > self.ranks[yRoot]:
            self.roots[yRoot] = xRoot
        elif self.ranks[xRoot] < self.ranks[yRoot]:
            self.roots[xRoot] = yRoot
        else:
            self.roots[yRoot] = xRoot
            self.ranks[xRoot] += 1

    def isConnected(self) -> bool:
        return self.n == 1


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        unionFind = UnionFind(n)
        factorIndices = {}
        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if f in factorIndices:
                        unionFind.union(i, factorIndices[f])
                    else:
                        factorIndices[f] = i
                    while num % f == 0:
                        num //= f
                f += 1
            if num > 1:
                if num in factorIndices:
                    unionFind.union(i, factorIndices[num])
                else:
                    factorIndices[num] = i
        return unionFind.isConnected()



