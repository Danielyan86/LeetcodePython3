from typing import List


class LinkNode:
    def __init__(self, value):
        self.next = None
        self.value = value


class SingleLink:
    def __init__(self, size=0):
        self.size = size
        self.head = None
        self.tail = None
        self.current_node_number = 0

    def insert(self, value, current_node=None):
        pass

    def add_value_to_tail(self, value):
        if self.head is None:
            self.head = self.tail = LinkNode(value)
        else:
            current_node = LinkNode(value)
            self.tail.next = current_node
            self.tail = current_node

    def insert_value_by_asc(self, value):
        if self.head is None:
            self.head = self.tail = LinkNode(value)
        else:
            new_node = LinkNode(value)
            if value < self.head.value:
                new_node.next = self.head
                self.head = new_node
                return
            if value > self.tail.value:
                self.tail.next = new_node
                self.tail = new_node
                return
            current_node = self.head
            while current_node:
                if current_node.value < value <= current_node.next.value:
                    new_node.next = current_node.next
                    current_node.next = new_node
                current_node = current_node.next

    def is_loop(self):
        if self.head is None:
            return False
        if self.size == 1:
            return False
        slow_pointer = fast_pointer = self.head
        while fast_pointer and fast_pointer.next:

            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer is slow_pointer:
                return True
        return False

    def traverse_link(self):
        if self.head is None:
            print("this is an empty link")
        else:
            current_node = self.head
            print("start to traverse link")
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def generate_link(self, num_list: List[int]):
        self.head = LinkNode(num_list[0])
        node = self.head
        if len(num_list) > 1:
            for num in num_list[1:]:
                node.next = LinkNode(num)
                node = node.next

    def merge_links(self):
        pass

    def get_node_by_value(self, value):
        if self.head is None:
            return None
        node = self.head
        while node:
            if node.value == value:
                return node
            else:
                node = node.next
        return None

    def reverse_like(self):
        if self.head is None:
            return None
        new_tail = new_head = self.head
        next_node = self.head.next
        new_tail.next = None
        while next_node:
            temp_node = next_node
            next_node = next_node.next
            temp_node.next = new_head
            new_head = temp_node
        self.head, self.tail = new_head, new_tail


if __name__ == '__main__':
    new_link = SingleLink(10)
    new_link.add_value_to_tail(2)
    new_link.add_value_to_tail(1)
    new_link.add_value_to_tail(3)
    new_link.traverse_link()

    new_link_2 = SingleLink(10)
    new_link_2.insert_value_by_asc(2)
    new_link_2.insert_value_by_asc(1)
    new_link_2.insert_value_by_asc(3)
    new_link_2.insert_value_by_asc(10)
    new_link_2.insert_value_by_asc(100)
    new_link_2.insert_value_by_asc(50)

    new_link_2.traverse_link()
    new_link_2.reverse_like()
    new_link_2.traverse_link()

    new_link_3 = SingleLink(10)
    new_link_3.insert_value_by_asc(2)
    new_link_3.insert_value_by_asc(1)
    new_link_3.traverse_link()

    new_link_4 = SingleLink(10)
    new_link_4.generate_link(list(range(5)))
    new_link_4.traverse_link()

    new_link_4 = SingleLink(10)
    new_link_4.generate_link([3, 4, 6, 10])
    new_link_4.traverse_link()
