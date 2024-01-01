class Solution2(object):
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            start = max(i - len(res) - 1, 0)
            temp = s[start : i + 1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
