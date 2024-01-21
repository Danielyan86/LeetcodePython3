# Definition for a binary tree node.
from typing import List, Optional

# 从上往下递归构造，比回溯大法更容易想到
# 根据前序数组的第一个元素，就可以确定根节点
# 用preorder[0]去中序数组中查找对应的元素

# 递归的处理前序数组的左边部分和中序数组的左边部分
# 递归处理前序数组右边部分和中序数组右边部分


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root_idx = inorder.index(root_val)

        root = TreeNode(root_val)
        root.left = self.buildTree(preorder, inorder[:root_idx])
        root.right = self.buildTree(preorder, inorder[root_idx + 1 :])

        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    res = s.buildTree(preorder, inorder)
    print(res)
