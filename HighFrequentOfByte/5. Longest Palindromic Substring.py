# 单指针遍历,从坐标0开始
# 每次只判断两个字符串
# 注意起始坐标要格外-1，是因为要大于当前最大的，所以要减一
# 一个是当前下标，一个是当前完后挪动一个
# 全部采用切片操作


class Solution:
    # 不要采用取巧的切片操作，多用变量
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            start = i - len(res) - 1 if i - len(res) - 1 > 0 else 0
            tmp1, tmp2 = s[start : i + 1], s[start + 1 : i + 1]
            if tmp1 == tmp1[::-1]:
                res = tmp1
            elif tmp2 == tmp2[::-1]:
                res = tmp2
        return res
