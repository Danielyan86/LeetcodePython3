class LinkNode:
    def __init__(self, key=0, value=0):
        self.key = key  # 再存一遍key是为了反向找到字典中的key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        # 设置一个fake头部和尾部节点，所谓的fake节点，也就是不会计入cache节点，
        # 但是这样有个好处是让双向链表的头尾节点的增删更为容易，也就是每次都是操作链表中间的节点，不用每次都去判断链表的是否有头尾节点
        self.tail = self.head = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove_from_link(node)
            self.attach_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.key, node.value = key, value
            self.remove_from_link(node)
            self.attach_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                self.remove_tail()
            node = LinkNode(key, value)
            self.attach_to_head(node)
            self.cache[key] = node

    def remove_from_link(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None
        del self.cache[node.key]

    # because there is already a fake head node, just to attach this node to the second node behind the fake node
    def attach_to_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        self.cache[node.key] = node

    def remove_tail(self):
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        node.prev = node.next = None
        del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(2, 2)
    l_dic = lRUCache.cache
    for key in l_dic:
        print(l_dic[key].key, l_dic[key].value)
    lRUCache.put(3, 3)
    l_dic = lRUCache.cache
    for key in l_dic:
        print(l_dic[key].key, l_dic[key].value)
    lRUCache.get(2)
    # l_dic = lRUCache.cache
    # for key in l_dic:
    #     print(l_dic[key].key, l_dic[key].value)
    # lRUCache.put(4, 4)
    # l_dic = lRUCache.cache
    # for key in l_dic:
    #     print(l_dic[key].key, l_dic[key].value)
