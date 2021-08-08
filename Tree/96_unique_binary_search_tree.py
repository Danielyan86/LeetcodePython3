# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def num_trees(self, n: int):
        ans = {0: 1,
               1: 1,
               2: 2
               }
        return self.helper(n, ans)

    def helper(self, n, ans):
        if n in ans:
            return ans[n]
        res = 0
        for i in range(n):
            res += self.helper(i, ans) * self.helper(n - i - 1, ans)
        ans[n] = res
        return res


if __name__ == '__main__':
    s = Solution()
    num = s.num_trees(3)
    print(num)
