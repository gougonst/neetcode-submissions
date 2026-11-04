class Solution:
    def reverse(self, x: int) -> int:
        INT32_MAX = 2 ** 31 - 1
        INT32_MIN = -INT32_MAX - 1

        res = 0
        while x != 0:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            print(x)

            if res > INT32_MAX // 10 or (res == INT32_MAX // 10 and digit > INT32_MAX % 10):
                return 0
            if res < INT32_MIN // 10 or (res == INT32_MIN // 10 and digit < INT32_MIN % 10):
                return 0

            res = res * 10 + digit
        return res