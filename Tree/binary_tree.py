import queue


class TreeNode:
    """ 最小数据结构，一个节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    """how to use the node to create a binary tree"""

    # use the queue to store the node
    def __init__(self, value_list=[]):
        self.root = None
        for n in value_list:
            self.insert(n)

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
            return
        else:
            q = queue.Queue()
            q.put(self.root)
            while not q.empty():
                node = q.get()
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                else:
                    q.put(node.left)
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                else:
                    q.put(node.right)

    def traverse(self, root=None):
        if root:
            print(root.val)
            if root.left:
                self.traverse(root.left)
            else:
                return
            if root.right:
                self.traverse(root.right)
            else:
                return
        else:
            return

    def delete(self, value):
        pass

    def search(self, value):
        pass


if __name__ == '__main__':
    value_list = list(range(1, 10))
    print(value_list)
    b = BinaryTree(value_list)
    b.traverse(b.root)
