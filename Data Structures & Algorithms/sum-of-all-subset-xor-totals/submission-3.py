class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for num in nums:
            res |= num
        return res << (n - 1)