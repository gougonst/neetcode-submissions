class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        redBound, blueBound = 0, len(nums) - 1
        i = 0
        while i <= blueBound:
            color = nums[i]
            if color == 0:
                nums[redBound], nums[i] = nums[i], nums[redBound]
                redBound += 1
            elif color == 2:
                nums[blueBound], nums[i] = nums[i], nums[blueBound]
                blueBound -= 1
            else:
                i += 1
            i = max(i, redBound)
        return nums