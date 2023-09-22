# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = list()  # 存储最后结果
        if root is None:
            return result

        stack = list()  # 栈
        while stack or root:
            if root is not None:  # root不为空则入栈
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
