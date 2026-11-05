class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts, rightProducts = [1] * len(nums), [1] * len(nums)
        leftProducts[0], rightProducts[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)):
            l = i
            r = len(nums) - 1 - i
            leftProducts[l] = leftProducts[l - 1] * nums[l]
            rightProducts[r] = rightProducts[r + 1] * nums[r]

        ans = []
        for i in range(len(nums)):
            l = 1 if i == 0 else leftProducts[i - 1]
            r = 1 if i == len(nums) - 1 else rightProducts[i + 1]
            ans.append(l * r)
        return ans

        