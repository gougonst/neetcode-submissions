class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        permutations = []

        def backtrack(permutation: List[int], used: Set[int]) -> None:
            if len(permutation) == n:
                permutations.append(permutation.copy())
                return
            
            for num in nums:
                if num in used:
                    continue
                permutation.append(num)
                used.add(num)
                backtrack(permutation, used)
                permutation.pop()
                used.remove(num)

        backtrack([], set())
        return permutations