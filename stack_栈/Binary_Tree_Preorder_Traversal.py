# Definition for a binary tree node.
# 题目：给定一个二叉树，返回它的 前序 遍历。
# 解题思路，尝试用迭代法遍历。把节点存入栈数据结构
# 难点：刚开始把判定条件写成当前节点左右节点为空，把问题复杂花了，从一开始逻辑搞复杂了，直接判断当前节点为空不就行了么！
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
        if not root:
            return number_list
        nodes_stack = []
        current_node = root
        while current_node or nodes_stack:
              # 栈应该是存上一个节点，第一次是根节点
            while current_node.left:
                nodes_stack.append(current_node)
                number_list.append(current_node.val)
                current_node = current_node.left
            number_list.append(current_node.val)

            if nodes_stack:  # 变换方向
                while nodes_stack:
                    previous_node = nodes_stack.pop()
                    current_node = previous_node.right
                    if current_node:
                        break
                if current_node:
                    nodes_stack.append(current_node)
                    number_list.append(current_node.val)
            else:
                nodes_stack.append(current_node)
                number_list.append(current_node.val)
        return number_list


if __name__ == '__main__':
    node4 = TreeNode(4)
    node2 = TreeNode(2)
    node2.left = node4

    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    s_obj = Solution()
    res = s_obj.preorderTraversal(node1)
    print(res)
