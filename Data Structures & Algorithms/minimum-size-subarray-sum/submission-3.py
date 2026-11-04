class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = math.inf
        sumLeft, sumRight = nums[0], nums[0]
        l, r = 0, 0
        while r < len(nums) and r >= l:
            if sumRight - sumLeft + nums[l] < target:
                r += 1
                if r >= len(nums):
                    break
                sumRight += nums[r]
            else:
                minLen = min(minLen, r - l + 1)
                l += 1
                if l >= len(nums):
                    break
                sumLeft += nums[l]
        return 0 if minLen == math.inf else minLen
