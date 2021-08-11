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

    def traverse_link(self):
        if self.head is None:
            print("this is an empty link")
        else:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next

    def generate_link(self, num_list):
        pass

    def merge_links(self):
        pass


if __name__ == '__main__':
    new_link = SingleLink(10)
    new_link.add_value_to_tail(1)
    new_link.add_value_to_tail(2)
    new_link.add_value_to_tail(3)
    new_link.traverse_link()
