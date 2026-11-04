class FreqStack:

    def __init__(self):
        self._counts = {}
        self._maxCount = 0
        self._stacks = {}
        

    def push(self, val: int) -> None:
        count = 1 if val not in self._counts else self._counts[val] + 1
        self._counts[val] = count
        self._maxCount = max(self._maxCount, count)

        if count not in self._stacks:
            self._stacks[count] = []
        self._stacks[count].append(val)


    def pop(self) -> int:
        stack = self._stacks[self._maxCount]
        popValue = stack.pop()
        self._counts[popValue] -= 1
        self._maxCount = self._maxCount - 1 if not stack else self._maxCount
        return popValue
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()