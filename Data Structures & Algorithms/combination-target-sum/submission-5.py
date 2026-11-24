class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []

        def backtrack(i: int, remain: int, comb: List[int]) -> None:
            if i >= len(nums):
                return
            if remain < 0:
                return
            if remain == 0:
                combs.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(i, remain - nums[i], comb)
            comb.pop()
            backtrack(i + 1, remain, comb)

        backtrack(0, target, [])
        return combs