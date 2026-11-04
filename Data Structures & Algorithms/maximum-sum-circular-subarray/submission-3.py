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

"""
There are 2 possible solutions in this problem:
Case 1 => [x1, (x2, x3, x4), x5, x6]: Max subarray is (x2, x3, x4)
Case 2 => [x1, x2, x3), x4, x5, (x6]: Max subarray is (x6, x1, x2, x3)

By using kadane's algorithm, we can calculate global maximum and 
  global minimum bounded by [x1 ... x6].
And also we can know, if we can get the maximum subarray, then the
  remain nums will be formed as a minimum subarray.

Therefore=>
  In case 1: The answer must be global maximum
  In case 2: The answer must be total - global minimum

Edge case:
  If all of nums are negative, then the global minimum will equal to
    total, the global maximum will be the biggest num in nums. (but 
    stillsmaller than 0)
  The thing is, total - global minimum = 0 bigger than global maximum
    , which is incorrect.
  In order to handle this situation, if global maximum > 0, then use
    global maximum as the answer.
"""