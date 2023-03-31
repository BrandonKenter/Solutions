class MyQueue:

    def __init__(self):
        self.stack = []
        self.secondary = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack) - 1):
            self.secondary.append(self.stack.pop())
        re = self.stack.pop()
        for i in range(len(self.secondary)):
            self.stack.append(self.secondary.pop())
        return re

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()