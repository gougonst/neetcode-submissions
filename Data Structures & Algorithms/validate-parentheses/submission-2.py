class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftBrackets = ('(', '[', '{')
        for c in s:
            if c in leftBrackets:
                stack.append(c)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if not (left == '(' and c ==')'
                    or left == '[' and c == ']'
                    or left == '{' and c == '}'):
                    return False
        return not stack
