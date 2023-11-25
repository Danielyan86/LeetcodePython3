# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        if 0 == n:
            return
        self.p = preorder
        self.i = inorder
        return self.buildTree_heler(0, n - 1, 0, n - 1)

    def buildTree_heler(self, inorder_l, inorder_r, preorder_l, preorder_r):
        if inorder_l > inorder_r:
            return None

        node = TreeNode(self.p[preorder_l])
        i_root_index = self.i.index(self.p[preorder_l])
        left_tree_size = i_root_index - inorder_l
        node.left = self.buildTree_heler(inorder_l, i_root_index - 1, preorder_l + 1, preorder_l + left_tree_size)
        node.right = self.buildTree_heler(i_root_index + 1, inorder_r, preorder_l + left_tree_size + 1, preorder_r)
        return node


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    res = s.buildTree(preorder, inorder)
    print(res)
