class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        sign1dp, sign2dp = [0] * n, [0] * n
        flag1, flag2 = True, False

        sign1dp[n - 1] = 1
        sign2dp[n - 1] = 1

        maxSubarrayLen = 1

        def isValid(flag: bool, k: int) -> bool:
            return arr[k] > arr[k + 1] if flag else arr[k] < arr[k + 1]

        for k in range(n - 2, -1, -1):
            sign1dp[k] = 1 + sign1dp[k + 1] if isValid(flag1, k) else 1
            sign2dp[k] = 1 + sign2dp[k + 1] if isValid(flag2, k) else 1

            flag1 = not flag1
            flag2 = not flag2

            maxSubarrayLen = max(maxSubarrayLen, sign1dp[k], sign2dp[k])

        return maxSubarrayLen