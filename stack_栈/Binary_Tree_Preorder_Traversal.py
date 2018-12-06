# Definition for a binary tree node.
# 题目：给定一个二叉树，返回它的 前序 遍历。
# 解题思路，尝试用迭代法遍历。把节点存入栈数据结构
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        number_list = []
        node_stack = []
        if root:
            node_stack.append(root)
            number_list.append(root.val)
        while root:
            if root.left:
                number_list.append(root.left.val)
                node_stack.append(root.left)
                root = root.left
            elif root.right:
                number_list.append(root.right.val)
                node_stack.append(root.right)
                root = root.right
            else:
                # node_stack.pop()
                # node = node_stack[-1]
                # if node.right:
                #     number_list.append(node.right.val)
                #     root = node.right
                while len(node_stack) > 0:
                    node_stack.pop()  # 弹出当前节点，也就是没有左节点和右节点的末尾节点
                    node = node_stack[-1]
                    if node.right:
                        number_list.append(node.right.val)
                        root = node.right
                        break
        return number_list


if __name__ == '__main__':
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    s_obj = Solution()
    s_obj.preorderTraversal(node1)
