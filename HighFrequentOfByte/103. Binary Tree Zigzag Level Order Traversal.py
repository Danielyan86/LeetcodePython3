# 第一层的双端队列和程序遍历一样，不用再做特殊处理
# 关键点在于输出的队列，分成奇数偶数层即可
# 相当于从上层队列出来后，根据奇数偶数层规律一个一个放入tmp，再把tmp统一放入res即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = list()
        deque = collections.deque([root])
        while deque:
            tmp = []
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:  # 直接用res长度判断奇数偶数层，不用再单独用一个变量表示
                    tmp.append(node.val)  # 偶数层采用右边进
                else:
                    tmp = [node.val] + tmp  # 奇数层采用左边进
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(tmp)
        return res
