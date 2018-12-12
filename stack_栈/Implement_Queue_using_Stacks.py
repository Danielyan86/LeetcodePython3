class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self._data.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.empty():
            first_item = self._data[0]
            del self._data[0]
            return first_item

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self._data[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self._data:
            return False
        else:
            return True

if __name__ == '__main__':
    # Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
