class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtrack(i: int, combination: List[int], total: int):
            if total == target:
                combinations.append(combination.copy())
                return
            if i >= len(nums) or total > target:
                return
                
            combination.append(nums[i])
            backtrack(i, combination, total + nums[i])
            combination.pop()
            backtrack(i + 1, combination, total)

        backtrack(0, [], 0)
        return combinations            