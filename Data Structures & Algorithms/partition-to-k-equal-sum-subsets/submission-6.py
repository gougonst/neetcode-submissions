class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum
        #  => sum(nums) / k

        subsetSum = sum(nums) / k
        if subsetSum != int(subsetSum):
            return False

        nums.sort(reverse=True)
        used = ['0'] * len(nums)
        memo = {}

        def consumeSubsetNumbers(remain: int, i: int, k: int) -> bool:
            if k == 0:
                return True
            
            used_str = "".join(used)
            if used_str in memo:
                return memo[used_str]

            if remain == 0:
                memo[used_str] = consumeSubsetNumbers(subsetSum, 0, k - 1)
                return memo[used_str]
            elif remain < 0:
                return False

            for j in range(i, len(nums)):
                if used[j] == '1' or nums[j] > remain:
                    continue

                used[j] = '1'
                if consumeSubsetNumbers(remain - nums[j], j + 1, k):
                    return True
                used[j] = '0'
            
            return False

        return consumeSubsetNumbers(subsetSum, 0, k)