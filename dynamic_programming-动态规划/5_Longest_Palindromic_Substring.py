# 题目：给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
class Solution0:
    def longestPalindrome(self, s: str) -> str:
        # Center expand method is easy to be implemented and more efficient
        # 需要注意细节，尤其是把两种情况和到一个方法怎么写
        if len(s) < 2:
            return s
        start, end = 0, 0
        for i in range(len(s) - 1):
            left, right = self.expand_center(i, i, s)
            if right - left > end - start:
                start, end = left, right
            left, right = self.expand_center(i, i + 1, s)
            if right - left > end - start:
                start, end = left, right
        print(s[start:end])
        return s[start:end]

    def expand_center(self, left, right, s):
        while left > 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
        return left + 1, right - 1


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路：长度从大到小遍历每一个子串，再反转字符[::-1]串做比较，此方法效率低下
        if len(s) > 0:
            if s == s[::-1]:
                return s
            for i in range(len(s) - 1, 0, -1):
                for j in range(0, len(s) - i + 1):
                    sub_str = s[j : j + i]
                    if sub_str == sub_str[::-1]:
                        return sub_str
        else:
            return ""


class Solution2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 用start和end来表示字符串起始和结束下标，可以用一个二位数字来表示是否为回文
        # pa[start][end]=True 表示是回文
        # 初始化pa[start][end],  start=end时候表示单个字母，则为true，
        # 奇数个回文起点是start=end，偶数个回文起点是end = start +1
        # 长度从小到大
        s_len = len(s)
        if s_len > 0:
            longest_le, longest_str = 1, s[0]
            if s == s[::-1]:
                return s
            # 初始化数组
            pa = [[None for _ in range(s_len)] for _ in range(s_len)]
            for i in range(s_len):
                pa[i][i] = True
                if i < s_len - 1:
                    pa[i][i + 1] = True if s[i] == s[i + 1] else False
                    if pa[i][i + 1]:
                        longest_le, longest_str = 2, s[i : i + 2]

            for start in reversed(range(s_len)):
                for end in range(start + 1, s_len):
                    if (
                        pa[start + 1][end - 1]
                        and s[start] == s[end]
                        and pa[start][end] == None
                    ):
                        pa[start][end] = True
                        if end - start + 1 > longest_le:
                            longest_le, longest_str = (
                                end - start + 1,
                                s[start : end + 1],
                            )
            return longest_str
        else:
            return ""


def test_solution2():
    s_obj = Solution2()
    assert s_obj.longestPalindrome("babad") == "aba"
    assert s_obj.longestPalindrome("a") == "a"
    assert s_obj.longestPalindrome("abb") == "bb"
    assert s_obj.longestPalindrome("abcba") == "abcba"
    assert s_obj.longestPalindrome("") == ""
    assert s_obj.longestPalindrome("cbbd") == "bb"
    assert s_obj.longestPalindrome("abacab") == "bacab"


if __name__ == "__main__":
    s_obj = Solution0()
    res = s_obj.longestPalindrome("abacab")
    print(res)
