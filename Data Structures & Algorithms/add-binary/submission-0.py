class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = deque([])

        aLen, bLen = len(a), len(b)

        c = False
        cura, curb = aLen - 1, bLen - 1
        while cura >= 0 or curb >= 0:
            digit = 0
            if c:
                digit += 1
            if cura >= 0:
                digit += int(a[cura])
            if curb >= 0:
                digit += int(b[curb])
            c = digit >= 2
            ans.appendleft(str(digit % 2))

            cura -= 1
            curb -= 1
        if c:
            ans.appendleft("1")
        ans = list(ans)
        return "".join(ans)