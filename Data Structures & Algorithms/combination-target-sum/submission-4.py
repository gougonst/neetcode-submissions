class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []

        def backtrack(comb: List[int], remain: int, i: int) -> None:
            if i >= len(nums) or remain < 0:
                return
            if remain == 0:
                combs.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(comb, remain - nums[i], i)
            comb.pop()
            backtrack(comb, remain, i + 1)

        backtrack([], target, 0)
        return combs
            
