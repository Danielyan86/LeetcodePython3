# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 使用栈的数据结构解决这个问题的一个原因是binary tree的travseral order和处理数据oder不一致
    # 先travseral后处理，刚好符合stack的特性
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 当根节点不为空或者栈不为空，从根节点开始
        # 若有左节点，则一直压栈
        # 若无左节点，则弹出，访问右节点
        if not root:
            return []

        stack = []
        res = []

        while root or stack:
            # 一直向左子树走，每一次将当前节点保存到栈中
            # should be notice that the current node is None can go into else branch
            # None node is like 辅助节点，类似LRU双向链表的头尾辅助节点
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，证明走到了最左边，从栈中弹出节点加入结果数组
            # 开始对右子树重复上述过程。
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
