class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = int(n * (n + 1) / 2)
        remain = total
        for num in nums:
            remain -= num
        return remain