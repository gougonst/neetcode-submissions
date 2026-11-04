class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for mask in range(1 << n):
            xorSum = 0
            for i in range(n):
                if mask & (1 << i):
                    xorSum ^= nums[i]
            res += xorSum
        return res