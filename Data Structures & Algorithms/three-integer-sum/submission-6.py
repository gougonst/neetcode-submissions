class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        i = 0
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue

            complement = -num
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > complement:
                    r -= 1
                elif nums[l] + nums[r] < complement:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    while (
                        l < r 
                        and nums[l] + nums[r] == complement
                    ):
                        l += 1
        return ans
