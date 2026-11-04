class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        preMax, curMax = 0, 0
        step = 0

        for i in range(n):
            if i > preMax:
                preMax = curMax
                step += 1
            curMax = max(curMax, i + nums[i])

        return step
