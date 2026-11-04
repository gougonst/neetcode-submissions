class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sumOfRecord = 0
        stack = []
        for operation in operations:
            if operation == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif operation == "D":
                score = stack[-1] * 2
                stack.append(score)
            elif operation == "C":
                score = -stack.pop()
            else:
                score = int(operation.replace(",", ""))
                stack.append(score)
            sumOfRecord += score
        return sumOfRecord