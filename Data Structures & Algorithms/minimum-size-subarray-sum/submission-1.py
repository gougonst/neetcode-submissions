class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumToEnd = []
        curSum = 0
        for num in nums:
            curSum += num
            sumToEnd.append(curSum)

        l, r = len(sumToEnd) - 1, len(sumToEnd) - 1
        minLen = math.inf
        while l >= 0 and r >= l:
            subarraySum = sumToEnd[r] - sumToEnd[l] + nums[l]
            if subarraySum < target:
                l -= 1
            else:
                minLen = min(minLen, r - l + 1)
                r -= 1
        return 0 if minLen == math.inf else minLen