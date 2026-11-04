class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort here to avoid duplicate combinations
        # For example:
        #   candidates: [1, 2, 7, 1], target: 8
        #   [1, 7] is as same as [7, 1]
        candidates = sorted(candidates)
        combinations = []
        
        def backtrack(i: int, combination: List[int], total: int):
            if total == target:
                combinations.append(combination.copy())
                return
            if i >= len(candidates) or total > target:
                return

            combination.append(candidates[i])
            backtrack(i + 1, combination, total + candidates[i])
            combination.pop()

            # If we're going to skip the candidate, skip all of same candidates as well.
            # It can guarantee that duplicate candidate only be used once in previous step.
            while len(candidates) > i + 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, combination, total)

        backtrack(0, [], 0)
        return combinations