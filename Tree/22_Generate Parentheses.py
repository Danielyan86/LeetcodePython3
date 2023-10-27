class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 难点在于怎么回溯，想想二叉树的遍历
        ans = []

        def backtrack(S, left, right):
            # 递归处理当前状态，三种
            # 加完括号返回
            # 优先加左括号
            # 右括号数目不能大于左边
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
                # n为几对括号，对应左括号或者右括号总数
                # 先出现的第一种情况是（（（ ））），然后通过pop方式倒着遍历所有情况
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans
