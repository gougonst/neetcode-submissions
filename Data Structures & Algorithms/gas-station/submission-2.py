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
        
# 我們可以定義一個最窮點，這是遍歷整個路程，gas[i] - cost[i] 所能夠累計的最小值，這可能是一段子序列的合，我們稱其為最窮子序列。
# 對於這樣的值，如果在其後面還有可能出現累計虧損的情況，則違背了先前的假設，因為我們已經定義他是遍歷整個路程後的最窮點，若是還有虧損，則先前定義的最窮點就不該是最窮點，因此，在此最窮點之後的收益永遠都會是正的，直到最窮子序列前。
# 又，因為 totalGas >= 0，因此我們可以確定累計的收益必定會 >= 最窮子序列