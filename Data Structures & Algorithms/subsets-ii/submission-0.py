class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        subsets = []

        def backtrack(subset: List[int], i: int) -> None:
            # Return if i == n, push subset into subsets
            if i == n:
                subsets.append(subset.copy())
                return

            # Choose nums[i], backtrack with i + 1
            subset.append(nums[i])
            backtrack(subset, i + 1)

            # Not to choose nums[i], backtrack with i + 1
            # Skip all subsequent duplicates to prevent generating
            # duplicate subsets.
            # Ex. [1, 2, 2'] and [1, 2', 2]
            subset.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(subset, i + 1)

        backtrack([], 0)
        return subsets