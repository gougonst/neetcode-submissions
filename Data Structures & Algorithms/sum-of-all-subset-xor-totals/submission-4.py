class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        def combination(cur: int, subsetSum: int) -> None:
            nonlocal res

            if cur >= n:
                return
            for i in range(cur, n):
                xorSum = subsetSum ^ nums[i]
                res += xorSum
                combination(i + 1, xorSum)
        
        combination(0, 0)
        return res
            