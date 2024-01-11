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
