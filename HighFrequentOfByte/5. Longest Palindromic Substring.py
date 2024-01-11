#
class Solution2(object):
    # 单指针遍历,从坐标0开始
    # 每次只判断两个字符串
    # 注意起始坐标要格外-1，是因为要大于当前最大的，所以要减一
    # 一个是当前下标，一个是当前完后挪动一个
    # 全部采用切片操作

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # 如果起始下标小于0，则从0开始，
            # 起始位置应该大于之前已经存在的最大回文串长度
            start = i - len(res) - 1 if i - len(res) - 1 >= 0 else 0
            temp = s[start : i + 1]
            # 如果一个字符串已经是回文，不用再判断
            if temp == temp[::-1]:  # 分奇数和偶数两种情况，
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
