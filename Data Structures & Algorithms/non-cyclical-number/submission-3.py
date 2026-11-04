class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self._sumOfSquare(n)

        while fast != slow:
            slow = self._sumOfSquare(slow)
            fast = self._sumOfSquare(fast)
            fast = self._sumOfSquare(fast)

        return fast == 1

    def _sumOfSquare(self, n: int) -> int:
        output  = 0
        while n != 0:
            output += (n % 10) ** 2
            n = n // 10
        return output