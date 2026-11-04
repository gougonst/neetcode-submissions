class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = []
        while columnNumber:
            columnNumber -= 1
            title.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        title.reverse()
        return "".join(title)