class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = math.inf
        sumLeft, sumRight = 0, 0
        l = 0
        for r in range(len(nums)):
            sumRight += nums[r]
            while l < len(nums) and sumRight - sumLeft >= target:
                minLen = min(minLen, r - l + 1)
                sumLeft += nums[l]
                l += 1
        return minLen if minLen != math.inf else 0