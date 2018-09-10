# 题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：
        if len(s) > 0:
            if s == s[::-1]:
                return s
            for i in range(len(s) - 1, 0, -1):
                for j in range(0, len(s) - i + 1):
                    sub_str = s[j:j + i]
                    if sub_str == sub_str[::-1]:
                        return sub_str
        else:
            return ""


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.longestPalindrome("abcba")
    print(res)
