# 中心扩散法，注意处理两种回文情况
# 先写中心扩散法，这个方法要被调用两次
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_center(s, l, r):
            if l == r:
                tmp = s[l]
            else:
                tmp = s[l] + s[r]
            l, r = l - 1, r + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    tmp = s[l] + tmp + s[r]
                    l, r = l - 1, r + 1
                else:
                    return tmp
            return tmp

        if len(s) == 1:
            return s
        max_str = ""
        for i in range(len(s) - 1):
            tmp1 = expand_center(s, i, i)

            if s[i] == s[i + 1]:
                tmp2 = expand_center(s, i, i + 1)
            max_str = max(tmp1, tmp1, key=len, default="")

        return max_str
