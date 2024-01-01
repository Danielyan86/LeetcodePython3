# 使用两个双向队列
# 用tmp控制出栈顺序
# 相当于从上层队列出来后，根据奇数偶数层规律一个一个放入tmp，再把tmp统一放入res即可
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:
                    tmp.append(node.val)  # 奇数层 -> 插入队列尾部
                else:
                    tmp.appendleft(node.val)  # 偶数层 -> 插入队列头部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res
