class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorResult = n
        for i in range(n):
            xorResult ^= i ^ nums[i]
        return xorResult