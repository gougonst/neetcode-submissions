class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums: Dict[int, int] = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevNums:
                return [prevNums[diff], i]
            prevNums[num] = i