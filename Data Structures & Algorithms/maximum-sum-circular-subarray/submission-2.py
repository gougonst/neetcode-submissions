class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMin, curMax = 0, 0
        globalMin, globalMax = nums[0], nums[0]
        total = 0
        
        for n in nums:
            curMin = min(n, curMin + n)
            curMax = max(n, curMax + n)
            globalMin = min(globalMin, curMin)
            globalMax = max(globalMax, curMax)
            total += n
        return max(globalMax, total - globalMin) if globalMax >= 0 else globalMax