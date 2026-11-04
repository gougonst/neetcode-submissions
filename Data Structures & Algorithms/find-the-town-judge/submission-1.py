class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trustMap = collections.defaultdict(set)
        citizens = set()
        for man, trusted in trust:
            trustMap[trusted].add(man)
            citizens.add(man)

        for candidate, trustors in trustMap.items():
            if len(trustors) == n - 1 and candidate not in citizens:
                return candidate
        return -1