class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxLen = 0

        for num in nums:
            # Find the head of the consecutive numbers
            if (num - 1) in uniqueNums:
                continue 

            length = 0
            while num in uniqueNums:
                length += 1
                num += 1
            maxLen = max(maxLen, length)
        
        return maxLen