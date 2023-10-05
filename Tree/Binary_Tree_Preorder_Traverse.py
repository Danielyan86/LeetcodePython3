# Definition for a binary tree node.
# 题目：给定一个二叉树，返回它的 前序 遍历。
# 解题思路，尝试用迭代法遍历。把节点存入栈数据结构
# 难点：合理利用两个while循环
# current node相当于一个指针
import Tree.binary_tree as tree


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
        current_node = root  # 先指向根节点
        while current_node or nodes_stack:
            while current_node:  # 一直找左节点，知道找不到为止
                nodes_stack.append(current_node)  # 节点存在，则入栈
                number_list.append(current_node.val)
                current_node = current_node.left  # 寻找左节点
            last_node = nodes_stack.pop()  # 寻找右 节点，左右两个节点已经找到，根节点没有用了，就弹出，这一步很关键
            current_node = last_node.right  # 右节点变成根节点，重新进入循环
        return number_list


if __name__ == "__main__":
    print(list(range(10)))
    tree_obj = tree.BinaryTree(list(range(10)))
    print(tree_obj.traverse_list)
    s_obj = Solution()
    res = s_obj.preorderTraversal(tree_obj.root)
    print(res)
