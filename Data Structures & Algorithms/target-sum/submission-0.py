class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums = collections.defaultdict(int)
        sums[0] = 1

        for num in nums:
            nextSums = collections.defaultdict(int)
            for s, count in sums.items():
                nextSums[s + num] = nextSums[s + num] + count
                nextSums[s - num] = nextSums[s - num] + count
            sums = nextSums
        return sums[target]