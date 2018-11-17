class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._data_min = []  # 降序栈
        self.min_index = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        if (not self._data_min) or x <= self._data_min[-1]:
            self._data_min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self._data:
            if self._data[-1] == self._data_min[-1]:
                self._data_min.pop()
            self._data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self._data:
            return self._data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self._data_min:
            return self._data_min[-1]


def test_minstack():
    obj = MinStack()
    obj.push(4)
    obj.push(6)
    obj.push(1)
    assert 1 == obj.top()
    assert 1 == obj.getMin()
    obj.pop()
    assert 6 == obj.top()
    assert 4 == obj.getMin()
    obj.push(1)
    obj.push(1)
    obj.push(1)


if __name__ == '__main__':
    obj = MinStack()
    obj.push(4)
    obj.push(6)
    obj.push(1)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_4)
