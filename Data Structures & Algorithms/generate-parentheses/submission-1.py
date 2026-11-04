class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def backtrack(parenthesis: str, status: int, used: int) -> None:
            if not status and used == n:
                parentheses.append(parenthesis)
                return

            if not status:
                parenthesis += '('
                backtrack(parenthesis, status + 1, used + 1)
            else:
                if used < n:
                    parenthesis += '('
                    backtrack(parenthesis, status + 1 , used + 1)
                    
                    parenthesis = parenthesis[:-1] + ')'
                    backtrack(parenthesis, status - 1, used)
                else:
                    parenthesis += ')'
                    backtrack(parenthesis, status - 1, used)

        backtrack("", 0, 0)
        return parentheses