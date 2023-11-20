class MyQueue:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> int:
        if self.B:
            return self.B.pop()
        self._move()
        return self.B.pop()

    def peek(self) -> int:
        if self.B:
            return self.B[-1]
        self._move()
        return self.B[-1]

    def _move(self):
        while self.A:
            self.B.append(self.A.pop())

    def empty(self) -> bool:
        return not (self.A or self.B)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
class MyQueue2(object):
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        if not self.empty():
            first_item = self._data[0]
            del self._data[0]
            return first_item

    def peek(self):
        if not self.empty():
            return self._data[0]

    def empty(self):
        if self._data:
            return False
        else:
            return True
