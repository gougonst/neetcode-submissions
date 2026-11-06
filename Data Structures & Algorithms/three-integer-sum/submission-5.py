class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        i = 0
        while i < len(nums):
            complement = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > complement:
                    r -= 1
                elif nums[l] + nums[r] < complement:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while (
                        l < r 
                        and nums[l] + nums[r] == complement
                    ):
                        l += 1
            prev = nums[i]
            while i < len(nums) and nums[i] == prev:
                i += 1
        return ans
