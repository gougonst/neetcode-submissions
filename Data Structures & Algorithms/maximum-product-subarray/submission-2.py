class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf

        maxProd = 1
        minProd = 1

        for num in nums:
            tmp = maxProd
            maxProd = max(num, num * maxProd, num * minProd)
            minProd = min(num, num * tmp, num * minProd)\

            res = max(res, maxProd)
        return res