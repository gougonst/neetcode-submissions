class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset: List[int], idx: int):
            res.append(subset.copy())
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()

        backtrack([], 0)
        return res
