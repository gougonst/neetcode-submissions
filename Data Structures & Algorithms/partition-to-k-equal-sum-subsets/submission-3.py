class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # Calculate the sum
        #  => sum(nums) / k

        subsetSum = sum(nums) / k
        if subsetSum != int(subsetSum):
            return False

        numCount = defaultdict(int)
        for num in nums:
            numCount[num] += 1
        sortNum = sorted(list(set(nums)), reverse=True)

        def consumeSubsetNumbers(remain: int) -> bool:
            if remain == 0:
                return True
            elif remain < 0:
                return False

            for num in sortNum:
                if numCount[num] <= 0:
                    continue

                numCount[num] -= 1
                if consumeSubsetNumbers(remain - num):
                    return True
                numCount[num] += 1
            
            return False

        for _ in range(k):
            if not consumeSubsetNumbers(subsetSum):
                return False

        for num, count in numCount.items():
            if count != 0:
                return False

        return True