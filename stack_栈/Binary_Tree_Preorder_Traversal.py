# Definition for a binary tree node.
# 题目：给定一个二叉树，返回它的 前序 遍历。
# 解题思路，尝试用迭代法遍历。把节点存入栈数据结构
# 难点：合理利用两个while循环
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
            while current_node:  # 左节点为none，跳出第二层循环
                nodes_stack.append(current_node)  # 节点存在，则入栈
                number_list.append(current_node.val)
                current_node = current_node.left  # 寻找左节点
            last_node = nodes_stack.pop()  # 寻找右 节点
            current_node = last_node.right  # 即使右节点为none，还是给当前值，这样不会再次进入寻找左节点的第二层循环，继续弹出栈的最后一个值
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
