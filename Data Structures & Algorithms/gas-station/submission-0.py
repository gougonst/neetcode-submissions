class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remains = [gas[i] - cost[i] for i in range(n)]
        start = 0

        for _ in range(n):
            end = start + n - 1
            remain = 0
            for i in range(start, end + 1):
                i = i % n
                remain += remains[i]
                if remain < 0:
                    start = i + 1
                    break

            if remain >= 0:
                return start

        return -1