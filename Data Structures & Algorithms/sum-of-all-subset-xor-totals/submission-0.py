class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def backtrack(start: int, subset: List[int]):
            nonlocal res
            xorSum = 0
            for num in subset:
                xorSum ^= num
            res += xorSum

            for j in range(start, len(nums)):
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res