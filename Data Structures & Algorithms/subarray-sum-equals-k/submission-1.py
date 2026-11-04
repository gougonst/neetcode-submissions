class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixCount = collections.defaultdict(int, { 0: 1 })

        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k
            if diff in prefixCount:
                res += prefixCount[diff]
            prefixCount[curSum] += 1
        
        return res
