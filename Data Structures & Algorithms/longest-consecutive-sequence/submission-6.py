class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinctNums = set(nums)
        longestLength = 0

        for num in distinctNums:
            if num - 1 in distinctNums:
                continue

            length = 0
            while num in distinctNums:
                num += 1
                length += 1
            longestLength = max(longestLength, length)
        return longestLength
