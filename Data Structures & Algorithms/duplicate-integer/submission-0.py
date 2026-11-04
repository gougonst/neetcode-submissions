class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques: Set[int] = set()
        for num in nums:
            if num in uniques:
                return True
            uniques.add(num)
        return False