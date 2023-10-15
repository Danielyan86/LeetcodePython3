# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder,self.inorder=preorder,inorder
        n=len(preorder)
        self.index={ele:i for i, ele in enumerate(inorder)}
        return self.helper_build_tree(0,n-1,0,n-1)

    def helper_build_tree(self,preorder_left, preorder_right, inorder_left, inorder_right):
        if preorder_left > preorder_right:
            return None
        
        preorder_root = preorder_left
        inorder_root = self.index[self.preorder[preorder_root]]
        root = TreeNode(self.preorder[preorder_root])

        size_left_subtree=inorder_root - inorder_left
        root.left = self.helper_build_tree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
        root.right = self.helper_build_tree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
        return root