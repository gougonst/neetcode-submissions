class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= dest:
                dest = i
        return dest == 0