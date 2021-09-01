#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
class Node:
    def __init__(self, key, value):
        self.pre = None
        self.next = None
        self.key = key  # 通过key才能反向找到字典的key
        self.value = value


class LRU_Link:
    def __init__(self, size):
        self.link_dict = {}
        self.size = size
        self.head = self.tail = None

    def set_new_node(self, key, value):
        new_node = Node(key, value)
        self.link_dict[key] = new_node
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.head.pre = new_node
        new_node.next = self.head
        self.head = new_node
        if len(self.link_dict) > self.size:
            last_node = self.tail
            last_node.pre.next = None
            self.tail = last_node.pre
            print(f"delete the node {last_node.key}")
            del self.link_dict[last_node.key]

    def get_value(self, key):
        if key in self.link_dict:
            node = self.link_dict[key]

            if node is self.head:
                return node.value
            elif node is self.tail:
                pre_node = node.pre
                pre_node.next = None
                self.tail = pre_node
            else:
                pre_node = node.pre
                next_node = node.next
                pre_node.next = next_node
                next_node.pre = pre_node
            node.pre = None  # move node to head
            node.next = self.head
            self.head.pre = node
            self.head = node
            return node.value
        else:
            return -1


class Solution:
    def LRU(self, operators, k):
        l_link = LRU_Link(k)
        get_list = []
        for oper in operators:
            if oper[0] == 1:
                key, value = oper[1], oper[2]
                l_link.set_new_node(key, value)
            elif oper[0] == 2:
                key = oper[1]
                get_list.append(l_link.get_value(key))
        return get_list


if __name__ == '__main__':
    s = Solution()
    res = s.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3)
    print(res)
