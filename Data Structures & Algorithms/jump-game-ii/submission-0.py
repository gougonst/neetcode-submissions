class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, 0
        step = 0

        while end < n - 1:
            nextEnd = 0
            for i in range(start, end + 1):
                nextEnd = max(nextEnd, nums[i] + i)
            step += 1
            start = end + 1
            end = nextEnd

        return step
