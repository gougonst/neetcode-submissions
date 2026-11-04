class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remains = [gas[i] - cost[i] for i in range(n)]
        start = 0
        curGas, totalGas = 0, 0

        for i in range(n):
            curGas += remains[i]
            totalGas += remains[i]

            if curGas < 0:
                start = i + 1
                curGas = 0
        return start if totalGas >= 0 else -1
        