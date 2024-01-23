from typing import List

# 回溯大法
# 停止的条件是n*2
# 为什么用list，方便pop


# 两个细节需要注意，S是个单个左右括号组成的list，需要用join函数合成一个string
# 传入左右括号数目时候，不能够先加一再传入，看起来好像一样，但是这样这样影响了当前一层函数中left的值，只能是传入参数时候+1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def traceback(left, right, lst):
            if len(lst) == n * 2:
                res.append("".join(lst))
            if left < n:
                lst.append("(")
                traceback(left + 1, right, lst)
                lst.pop()
            if right < left:
                lst.append(")")
                traceback(left, right + 1, lst)
                lst.pop()

        traceback(0, 0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(3)
