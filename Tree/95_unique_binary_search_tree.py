# 定义：二叉查找树，又被称为二叉搜索树。其特点如下：设x为二叉查找树中的一个结点，x节点包含关键字key，一句话就是左孩子比父节点小，右孩子比父节点大，
# 还有一个特性就是”中序遍历“可以让结点有序。

# 思路，先要明白什么是二叉搜索树。生成二叉搜索树，然后按照前序遍历方法输出成list集合
# 为什么前序遍历有NULL？
# 返回是一个根节点list集合，而不是例题中嵌套的list
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.get_trees(1, n)

    def get_trees(self, start, end) -> List:
        # 这个方法实际上是用来生成二叉树根节点集合的,
        # recursive solve this problem
        # 通过递归方法，先生成左边节点，再生成右边节点，最后挂在根节点上面，
        # 如果左边不是一个单节点而是一个数，就继续递归，直到只是一个单节点为止
        # 这个题难点是边界值判断
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end + 1):  # 遍历元素，相当于把集合里面元素挨个放到根节点进行遍历
            # i刚好是当前节点，左边范围是1到i，右边是i+1 到结束
            lefts = self.get_trees(start, i - 1)
            rights = self.get_trees(i + 1, end)
            for j in range(len(lefts)):
                for k in range(len(rights)):
                    # root point
                    root = TreeNode(i)
                    root.left = lefts[j]
                    root.right = rights[k]
                    res.append(root)
        return res


if __name__ == '__main__':
    s = Solution()
    tree_node_list = s.generateTrees(3)
    for l in tree_node_list:
        print(l.val)
