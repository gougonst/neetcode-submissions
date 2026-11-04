class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1

        tn = 0
        tn1 = 1
        tn2 = 1

        tn3 = 0
        for i in range(3, n + 1):
            tn3 = tn + tn1 + tn2
            tn, tn1, tn2 = tn1, tn2, tn3
        return tn3