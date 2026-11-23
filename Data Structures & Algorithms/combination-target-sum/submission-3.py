class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []

        def backtrack(i: int, comb: List[int], remain: int) -> None:
            if i >= len(nums) or remain < 0:
                return
            if remain == 0:
                combs.append(comb.copy())
                return

            comb.append(nums[i])
            backtrack(i, comb, remain - nums[i])
            comb.pop()
            backtrack(i + 1, comb, remain)

        backtrack(0, [], target)
        return combs
            
