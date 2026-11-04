class UnionFind:
    def __init__(self, n: int):
        self._root = [i for i in range(n)]
        self._rank = [0] * n

    def find(self, x: int) -> int:
        if self._root[x] != x:
            self._root[x] = self.find(self._root[x])
        return self._root[x]

    def union(self, x1: int, x2: int) -> None:
        root1, root2 = self.find(x1), self.find(x2)

        if root1 == root2:
            return

        if self._rank[root1] < self._rank[root2]:
            self._root[root1] = root2
        elif self._rank[root1] > self._rank[root2]:
            self._root[root2] = root1
        else:
            self._root[root2] = root1
            self._rank[root1] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(accounts))

        emailToAccount = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    unionFind.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i

        emailGroups = defaultdict(list)
        for email, idx in emailToAccount.items():
            i = unionFind.find(idx)
            emailGroups[i].append(email)

        res = []
        for idx, emails in emailGroups.items():
            name = accounts[idx][0]
            mergedEmails = sorted(emails)
            res.append([name] + mergedEmails)
        return res




