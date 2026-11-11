class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            elif nums[r] < nums[m]:
                l = m + 1
            else:
                r = m
        