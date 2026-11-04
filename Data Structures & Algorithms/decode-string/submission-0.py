class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def dfs(cur: str) -> str:
            nonlocal i
            if i >= len(s):
                return cur

            if s[i].isdigit():
                repeatTimes = ""
                while i < len(s) and s[i].isdigit():
                    repeatTimes += s[i]
                    i += 1
                repeatTimes = int(repeatTimes)
                cur += dfs("") * repeatTimes
                return dfs(cur)
            elif s[i].isalpha():
                while i < len(s) and s[i].isalpha():
                    cur += s[i]
                    i += 1
                return dfs(cur)
            elif s[i] == '[':
                i += 1
                return dfs(cur)
            elif s[i] == ']':
                i += 1
                return cur

        return dfs("")