class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        l, r = 0, len(nums) - 1
        while r >= 0 and nums[r] == val:
            r -= 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]

            l += 1
            while nums[r] == val:
                r -= 1

        return r + 1
        