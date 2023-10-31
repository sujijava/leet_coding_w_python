class MinStack:
    def __init__(self):
        self.A = []
        self.M = []

    def push(self, val: int) -> None:
        self.A.append(val)
        m = min(self.M[-1] if self.M else val, val)
        self.M.append(m)

    def pop(self) -> None:
        self.A.pop()
        self.M.pop()

    def top(self) -> int:
        return self.A[-1]

    def getMin(self) -> int:
        return self.M[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
