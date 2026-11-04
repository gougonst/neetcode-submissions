class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        plusOneDigits = collections.deque()
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry

            carry = digit // 10
            plusOneDigits.appendleft(digit % 10)

        if carry == 1:
            plusOneDigits.appendleft(1)

        return list(plusOneDigits)