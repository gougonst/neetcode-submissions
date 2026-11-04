class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []

        i = 0
        while i < n:
            c = s[i]

            if c.isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                stack.append(int(num))
            elif c == '[':
                continue
            elif c == ']':
                word = ""
                while not isinstance(stack[-1], int):
                    word = stack.pop() + word
                freq = int(stack.pop())
                stack.append(word * freq)
            else:
                stack.append(c)
            i += 1

        return ''.join(stack)