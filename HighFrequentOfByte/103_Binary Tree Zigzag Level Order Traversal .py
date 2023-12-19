# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # to clear the way in-out direction of left and right
        # 利用双端队列性质，只要保证每次进入队列是按照一行顺序进入，至于怎么进入不重要，因为两端都可以进出
        # 因为是双端队列，记住左边弹出右边进入，反之亦然
        # 注意下层节点顺序，左边弹出时候，下层是先左后右，反之亦然
        if root is None:
            return []
        que = collections.deque([root])
        res = []
        while que:
            tmp = []
            for _ in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp)
            if not que:
                return res

            tmp = []
            for _ in range(len(que)):
                node = que.pop()
                tmp.append(node.val)
                if node.right:
                    que.appendleft(node.right)
                if node.left:
                    que.appendleft(node.left)
            res.append(tmp)
        return res
