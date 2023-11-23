### 需要注意几点

- 无论是 put 还是 get，都是往头节点添加，没有朝末尾节点添加的操作，末尾节点只有删除操作
- 一共三个方法，删除任意一个节点，添加头节点，删除末尾节点，add node 方法没法通用，因为没法确定要删除哪个位置节点
-

### use buildin OrderDict

```python
from collections import OrderedDict

class LRUCache:
    #let's assume the fist item is the less used due to orderedDict feature
    def __init__(self, capacity: int):
        self.capacity = capacity
        # OrderedDict maintains the insertion order of items
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # need to judge the key existing in dictionary d[k]=v is enough
        self.cache[key] = value # add to the end by default
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # pop the first item

```
