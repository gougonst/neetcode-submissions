class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TODO: Handle empty nums
        
        maxVal = nums[0]
        curSum = nums[0]
        for num in nums[1:]:
            if curSum < 0:
                curSum = num
            else:
                curSum += num
            maxVal = max(maxVal, curSum)
        return maxVal