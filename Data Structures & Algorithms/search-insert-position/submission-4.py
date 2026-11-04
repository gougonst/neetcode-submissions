class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Use binary search to find the most close (bigger) one
        # r must be len(nums) rather than len(nums) - 1 because
        #   the search range is between [0, len(nums)], included
        #   the target bigger than nums[len(nums) - 1] scenario.
        l, r = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1

        return l