class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Use binary search to find the most close (bigger) one
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m
            elif nums[m] < target:
                l = m + 1

        return len(nums) if target > nums[len(nums) - 1] else r