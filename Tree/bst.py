#  二叉搜索树定义
# 二叉搜索树(Binary Search Tree)，又名二叉排序树(Binary Sort Tree)。
# 二叉搜索树是具有有以下性质的二叉树：
# （1）若左子树不为空，则左子树上所有节点的值均小于或等于它的根节点的值。
# （2）若右子树不为空，则右子树上所有节点的值均大于或等于它的根节点的值。
# （3）左、右子树也分别为二叉搜索树。
#  （4）如果按照中序遍历

# 如何生成一个1到n的全部二叉搜索树树？
# 根据二叉树的性质，右节点比根节点大，左节点比根节点小，将进行分范围传入
# 如果是一个有序数组，有点triky的地方是二叉搜索树不是一个固定的树，
# 因此即使同一组数放进二叉搜索树也会有多种组合，如何生成所有组合呢？
# 根据二叉搜索树性质可以将有序数组分段传入，如果只有一个数了，就可以插入
import random


class TreeNode:
    """ 最小数据结构，一个节点"""

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.traverse_list = []

    def add(self, value, node: TreeNode = None):
        if node:
            if value > node.val:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                else:
                    node = node.right
                    self.add(value, node)
            if value < node.val:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                else:
                    node = node.left
                    self.add(value, node)
        else:
            self.root = TreeNode(value)

    def get(self, val, node: TreeNode):
        if val > node.val and node.right is None:
            return node
        if val < node.val and node.left is None:
            return node

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


if __name__ == '__main__':
    bst_tree = BST()
    number_list = random.sample(range(1, 10), 9)  # generate

    print(number_list)
    for num in number_list:
        bst_tree.add(num, bst_tree.root)
    bst_tree.middle_order_traverse(bst_tree.root)
    print(bst_tree.traverse_list)
