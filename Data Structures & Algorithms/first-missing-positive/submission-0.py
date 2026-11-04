class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Find the smallest:
        #   For each positive number, min(minPositive, number - 1)
        # If the smallest positive number is 0, use index sort

        n = len(nums)

        minPositive = math.inf
        for num in nums:
            if num > 0:
                minPositive = min(minPositive, num - 1)

        if minPositive > 0:
            return 1

        for i, num in enumerate(nums):
            while (num > 0 and num <= n and
                   i != num - 1 and
                   num != nums[num - 1]):
                nums[i], nums[num - 1] = nums[num - 1], nums[i]
                num = nums[i]
        
        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1
        return n + 1
