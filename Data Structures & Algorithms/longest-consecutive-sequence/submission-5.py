class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        numLength = dict([(num, 1) for num in nums])

        def dfs(num: int) -> int:
            if num not in numLength:
                return 0
            if numLength[num] != 1:
                return numLength[num]
            numLength[num] = 1 + dfs(num + 1)
            return numLength[num]

        longestLength = 0
        for num in nums:
            longestLength = max(longestLength, dfs(num))
        return longestLength
