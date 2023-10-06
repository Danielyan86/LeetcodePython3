import queue
from typing import Optional


class TreeNode:
    """最小数据结构，一个节点"""

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

    def insert_BST(self, node, value):
        if node:
            if value > node.val:
                if node.right:
                    self.insert_BST(node.right, value)
                else:
                    node.right = TreeNode(value)
            else:
                if node.left:
                    self.insert_BST(node.left, value)
                else:
                    node.left = TreeNode(value)

        return

    # 前中后三种方式遍历代码是一样的，只是打印值代码位置不一样
    # 递归方式dsf 策略进行遍历 因为每个节点都要走一次，打印或者说取值只需要一次
    # 前中后序刚好是取值这行代码在代码中的位置
    def preorder_traverse(self, root=None):
        if root is None:
            return
        # if the root is not None,it must have 2 sub-node
        # there is no need for extra condition for left or right tree judgement
        self.traverse_list.append(root.val)
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)

    def preorder_traverse_stack(self, root=None):
        if root is None:
            return
        BLACK, WHITE = 0, 1
        stack = list()
        stack.append((root, WHITE))
        while stack:
            node, color = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((node.right, WHITE))
                stack.append((node.left, WHITE))
                stack.append((node, BLACK))
            elif color == BLACK:
                self.traverse_list.append(node.val)

    def postorder_traverse(self, root=None):
        if root is None:
            return
        else:
            self.postorder_traverse(root.left)
            self.postorder_traverse(root.right)
            self.traverse_list.append(root.val)

    def middleorder_traverse(self, root=None):
        if root is None:
            return
        else:
            self.middleorder_traverse(root.left)
            self.traverse_list.append(root.val)
            self.middleorder_traverse(root.right)

    def middleorder_traverse_stack(self, root=None):
        if root is None:
            return
        BLACK, WHITE = 0, 1
        stack = list()
        stack.append((root, WHITE))
        while stack:
            node, color = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((node.right, WHITE))
                stack.append((node, BLACK))
                stack.append((node.left, WHITE))
            elif color == BLACK:
                self.traverse_list.append(node.val)

    def delete(self, value):
        pass

    def search(self, value):
        pass

    def empty_traverse_list(self):
        self.traverse_list = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        num_res = []
        BLACK, WHITE = 0, 1
        res = True
        stack.append((root, WHITE))
        while stack:
            node, color = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((node.right, WHITE))
                stack.append((node, BLACK))
                stack.append((node.left, WHITE))
            else:
                num_res.append(node.val)
                if len(num_res) > 1:
                    print(num_res)
                    if num_res[-1] > num_res[-2]:
                        continue
                    else:
                        res = False
                        break
        return res


class Solution:
    num = float("-inf")
    res = True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        self.isValidBST(root.left)
        if root.val > Solution.num:
            Solution.num = root.val
        else:
            Solution.res = False
        self.isValidBST(root.right)
        return Solution.res


if __name__ == "__main__":
    value_list = list(range(1, 2))
    print(value_list)
    b = BinaryTree(value_list)
    for num in range(2, 4):
        b.insert_BST(b.root, num)

    # b.preorder_traverse(b.root)
    # print(b.traverse_list)

    # b.empty_traverse_list()
    # b.postorder_traverse(b.root)
    # print(b.traverse_list)

    # b.empty_traverse_list()
    # b.middleorder_traverse(b.root)
    # print(b.traverse_list)

    # b.empty_traverse_list()
    # b.preorder_traverse_stack(b.root)
    # print(b.traverse_list)

    b.empty_traverse_list()
    b.middleorder_traverse_stack(b.root)
    print(b.traverse_list)

    res = b.isValidBST(b.root)
    print(res)

    c = BinaryTree(range(1))
    s = Solution()
    res = s.isValidBST(c.root)
    print(res)
