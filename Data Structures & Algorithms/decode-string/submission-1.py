class Solution:
    def decodeString(self, s: str) -> str:
        stringStack = []
        countStack = []
        cur = ""
        count = 0

        for c in s:
            if c.isdigit():
                count = count * 10 + int(c)
            elif c == "[":
                stringStack.append(cur)
                countStack.append(count)
                cur = ""
                count = 0
            elif c.isalpha():
                # b2[a]
                # cur = a
                cur += c
            elif c == "]":
                # stack: [b]
                # stack: [2]

                # temp = a
                temp = cur
                cur = stringStack.pop()
                k = countStack.pop()
                cur += k * temp
            
        return cur