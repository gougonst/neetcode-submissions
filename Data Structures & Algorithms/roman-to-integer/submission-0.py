class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumeral = {}
        romanNumeral["I"] = (0, 1)
        romanNumeral["V"] = (1, 5)
        romanNumeral["X"] = (2, 10)
        romanNumeral["L"] = (3, 50)
        romanNumeral["C"] = (4, 100)
        romanNumeral["D"] = (5, 500)
        romanNumeral["M"] = (6, 1000)

        stack = []
        for c in s:
            stack.append(c)

        number = 0
        maxDigit = 0
        for roman in reversed(stack):
            romanDigit, romanNumber = romanNumeral[roman]
            if romanDigit < maxDigit:
                number -= romanNumber
            else:
                number += romanNumber
                maxDigit = romanDigit
        return number