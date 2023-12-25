# 题目：
# 使用队列实现栈的下列操作：
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._data.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if not self.empty():
            return self._data.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if not self.empty():
            return self._data[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self._data:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
