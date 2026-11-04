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
        n = len(nums)
        maxNum = max(nums)

        # Sieve of eratosthenes
        sieve = [0] * (maxNum + 1)
        for i in range(2, math.isqrt(maxNum) + 1):
            if sieve[i] == 0:
                for j in range(i * i, maxNum + 1, i):
                    sieve[j] = i

        unionFind = UnionFind(n + maxNum + 1)
        for i, num in enumerate(nums):
            while num > 1:
                prime = num if sieve[num] == 0 else sieve[num]
                unionFind.union(i, n + prime)
                while num % prime == 0:
                    num //= prime

        root = unionFind.find(0)
        for i in range(1, n):
            if unionFind.find(i) != root:
                return False
        return True
