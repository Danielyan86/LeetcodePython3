class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = []
        queue = collections.deque([root])
        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
