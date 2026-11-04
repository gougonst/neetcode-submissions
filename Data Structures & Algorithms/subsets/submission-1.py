class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(idx: int):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(idx + 1)

        backtrack(0)
        return res
