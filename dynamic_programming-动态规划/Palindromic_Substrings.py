# 题目：给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。


# 思路：和最长回文子串类似
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        countStr = s_len
        if s_len > 0:
            # 初始化数组
            pa = [[None for _ in range(s_len)] for _ in range(s_len)]
            for i in range(s_len):
                pa[i][i] = True
                if i < s_len - 1:
                    pa[i][i + 1] = True if s[i] == s[i + 1] else False
                    if pa[i][i + 1]:
                        countStr += 1

            for start in reversed(range(s_len)):
                for end in range(start + 1, s_len):
                    if (
                        pa[start + 1][end - 1]
                        and s[start] == s[end]
                        and pa[start][end] == None
                    ):
                        pa[start][end] = True
                        countStr += 1
            return countStr
        else:
            return 0


class Solution2:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        countStr = s_len
        if s_len > 1:
            s.join("*")
            return countStr
        else:
            return countStr


def test_solution():
    s_obj = Solution()
    assert s_obj.countSubstrings("abacab") == 9
    assert s_obj.countSubstrings("aaa") == 6
    assert s_obj.countSubstrings("abc") == 3


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.countSubstrings("abacab")
    print(res)
