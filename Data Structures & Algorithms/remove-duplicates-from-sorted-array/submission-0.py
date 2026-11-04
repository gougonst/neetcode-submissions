class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        l = 1
        prev = nums[0]
        for i, num in enumerate(nums):
            if num != prev:
                nums[l] = num
                l += 1
            prev = num
        return l