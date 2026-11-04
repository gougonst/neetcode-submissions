class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[r] == val:
                r -= 1
                continue

            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]

            l += 1

        return r + 1
        