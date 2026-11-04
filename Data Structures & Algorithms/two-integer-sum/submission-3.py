class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices: Dict[int, List[int]] = {}
        for i, num in enumerate(nums):
            if num not in numIndices:
                numIndices[num] = []
            numIndices[num].append(i)

        for i1, num in enumerate(nums):
            complement = target - num
            if complement not in numIndices:
                continue
            for i2 in numIndices[complement]:
                if i1 != i2:
                    return [i1, i2]
                    
        return None