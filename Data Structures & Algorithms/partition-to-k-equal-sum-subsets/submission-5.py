class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum
        #  => sum(nums) / k

        subsetSum = sum(nums) / k
        if subsetSum != int(subsetSum):
            return False

        nums.sort(reverse=True)
        used = [False] * len(nums)

        def consumeSubsetNumbers(remain: int, i: int, k: int) -> bool:
            if k == 0:
                return True
            if remain == 0:
                return consumeSubsetNumbers(subsetSum, 0, k - 1)
            elif remain < 0:
                return False

            for j in range(i, len(nums)):
                if used[j] or nums[j] > remain:
                    continue

                used[j] = True
                if consumeSubsetNumbers(remain - nums[j], j + 1, k):
                    return True
                used[j] = False
            
            return False

        return consumeSubsetNumbers(subsetSum, 0, k)