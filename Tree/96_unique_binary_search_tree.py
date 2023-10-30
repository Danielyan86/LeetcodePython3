# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def num_trees(self, n: int):
        ans = {0: 1, 1: 1, 2: 2}
        return self.helper(n, ans)

    def helper(self, n, ans):
        # recursive way to implement
        if n in ans:
            return ans[n]
        res = 0
        for i in range(n):
            res += self.helper(i, ans) * self.helper(n - i - 1, ans)
        ans[n] = res
        return res


class Solution2:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):  # i看成最右边节点的边界
            for j in range(1, i + 1):  # j可以看成对根节点的遍历
                G[i] += G[j - 1] * G[i - j]  # 笛卡尔积

        return G[n]


if __name__ == "__main__":
    s = Solution()
    num = s.num_trees(3)
    print(num)
