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
        self.traverse_list = []
        for n in value_list:
            self.insert(n)

    def insert(self, value):

        if self.root is None:
            self.root = TreeNode(value)
            return
        else:
            # 利用队列先进先出特性，构建完全二叉树
            # 初始化一个空队列，先把根节点放入队列
            # 根节点出队列，有子节点则进队列，相当于用迭代方式进行层次遍历，没有子节点则挂载，结束循环
            q = queue.Queue()
            q.put(self.root)
            while not q.empty():
                node = q.get()  # 出队列
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

    # 前中后三种方式遍历代码是一样的，只是打印值代码位置不一样
    def preorder_traverse(self, root=None):
        # 递归方式dsf 策略进行遍历
        if root:
            self.traverse_list.append(root.val)
            if root.left:
                self.preorder_traverse(root.left)
            else:
                return
            if root.right:
                self.preorder_traverse(root.right)
            else:
                return
        else:
            return

    def postorder_order_traverse(self, root_node):
        if root_node:
            if root_node.left:
                self.postorder_order_traverse(root_node.left)
            if root_node.right:
                self.postorder_order_traverse(root_node.right)
            self.traverse_list.append(root_node.val)
            return
        else:
            return

    def middle_order_traverse(self, root_node):
        if root_node:
            if root_node.left:
                self.middle_order_traverse(root_node.left)
            self.traverse_list.append(root_node.val)

            if root_node.right:
                self.middle_order_traverse(root_node.right)
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

    b.preorder_traverse(b.root)

    print(b.traverse_list)
    b.traverse_list = []
    b.postorder_order_traverse(b.root)
    print(b.traverse_list)
    b.traverse_list = []
    b.middle_order_traverse(b.root)
    print(b.traverse_list)
