class Solution2(object):
    # 单指针遍历
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # 如果起始下标小于0，则从0开始，
            # 起始位置应该大于之前已经存在的最大回文串长度
            start = i - len(res) - 1 if i - len(res) - 1 >= 0 else 0
            temp = s[start : i + 1]
            # 如果一个字符串已经是回文，不用再判断
            if temp == temp[::-1]:  # 分奇数和偶数两种情况，如果是偶数，else则是奇数，反之亦然
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
