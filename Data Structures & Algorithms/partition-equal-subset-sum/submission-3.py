class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False
        halfSum = totalSum // 2

        dp = {0}

        for num in nums:
            nextDP = dp.copy()
            for s in dp:
                if s + num == halfSum:
                    return True
                nextDP.add(s + num)
            dp = nextDP

        return False