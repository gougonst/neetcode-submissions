class MyQueue:

    def __init__(self):
        self._pushStack = collections.deque()
        self._popStack = collections.deque()

    def push(self, x: int) -> None:
        self._pushStack.append(x)

    def pop(self) -> int:
        self._swapPushPopStack()
        return self._popStack.pop()

    def peek(self) -> int:
        self._swapPushPopStack()
        return self._popStack[-1] if self._popStack else None

    def empty(self) -> bool:
        return not self._popStack and not self._pushStack

    def _swapPushPopStack(self) -> None:
        if self._popStack:
            return

        while self._pushStack:
            element = self._pushStack.pop()
            self._popStack.append(element)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()