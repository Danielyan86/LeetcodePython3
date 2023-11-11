# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def c(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        levels = 0
        que = collections.deque([root])
        while que:
            levels += 1
            # 计算长度，打到左出右进效果，比一次记录一层跟节省内存空间
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return levels
