class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, count = 0, 0
        for num in nums:
            if count == 0:
                majority = num
            count += (1 if majority == num else -1)
        return majority