# 题目：给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 解题思路：广度优先搜索二叉树变体，每层从左往右顺序变成了从左往右和从右往左交替进行
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        num_list = []
        if root:
            self.binary_tree_iterator(root, num_list, level=0)
        return num_list

    def binary_tree_iterator(self, binary_node, number_list, level):
        if level + 1 > len(number_list):
            number_list.append([binary_node.val])
        else:
            if level % 2 == 0:
                number_list[level].append(binary_node.val)
            else:
                number_list[level] = [binary_node.val] + number_list[level]
        level = level + 1
        if binary_node.left:
            self.binary_tree_iterator(binary_node.left, number_list, level)
        if binary_node.right:
            self.binary_tree_iterator(binary_node.right, number_list, level)


if __name__ == "__main__":
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node1.left = node2
    node1.right = node3
    s_obj = Solution()

    res = s_obj.zigzagLevelOrder(None)
    print(res)

    res = s_obj.zigzagLevelOrder(node2)
    print(res)

    res = s_obj.zigzagLevelOrder(node1)
    print(res)
