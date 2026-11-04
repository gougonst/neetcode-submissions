class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        sign1Len, sign2Len = 1, 1
        flag1, flag2 = True, False

        maxSubarrayLen = 1

        def isValid(flag: bool, k: int) -> bool:
            return arr[k] > arr[k + 1] if flag else arr[k] < arr[k + 1]

        for k in range(n - 2, -1, -1):
            sign1Len = 1 + sign1Len if isValid(flag1, k) else 1
            sign2Len = 1 + sign2Len if isValid(flag2, k) else 1

            flag1 = not flag1
            flag2 = not flag2

            maxSubarrayLen = max(maxSubarrayLen, sign1Len, sign2Len)

        return maxSubarrayLen