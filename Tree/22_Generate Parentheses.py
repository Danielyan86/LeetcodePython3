from typing import List


# 两个细节需要注意，S是个单个左右括号组成的list，需要用join函数合成一个string
# 传入左右括号数目时候，不能够先加一再传入，看起来好像一样，但是这样这样影响了当前一层函数中left的值，只能是传入参数时候+1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.back_trace(0, 0, [])
        return self.res

    def back_trace(self, left, right, S):
        if len(S) == self.n * 2:
            self.res.append("".join(S))
            return
        if left < self.n:
            S.append("(")
            self.back_trace(left + 1, right, S)
            S.pop()
        if right < left:
            S.append(")")
            self.back_trace(left, right + 1, S)
            S.pop()


if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(3)
