class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort(reverse=True)
        
        sumCombs = {}
        return self.dfs(nums, sumCombs, target, 0)

        
    def dfs(
        self,
        nums: List[int], 
        sumCombinations: Dict[int, List[List[int]]], 
        target: int, 
        i: int
    ) -> List[List[int]]:
        if target <= 0:
            return []

        if i >= len(nums):
            return []

        k = (target, i)
        if k in sumCombinations:
            return sumCombinations[k]

        if k not in sumCombinations:
            sumCombinations[k] = []

        if target < nums[i]:
            sumCombinations[k] = self.dfs(nums, sumCombinations, target, i + 1)
            return sumCombinations[k]

        maxUsage = target // nums[i]
        for usage in range(maxUsage, -1, -1):
            remain = target - usage * nums[i]
            if remain == 0:
                sumCombinations[k].append([nums[i]] * usage)
                continue

            combs = self.dfs(nums, sumCombinations, remain, i + 1)
            if not combs:
                continue
            for comb in combs:
                sumCombinations[k].append([nums[i]] * usage + comb)

        return sumCombinations[k]
        