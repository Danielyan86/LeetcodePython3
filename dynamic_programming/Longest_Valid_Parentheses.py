# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 关键点：利用有效子串的起始和结束的索引值来获取长度
        # @param s, a string
        # @return an integer
        # start开始记录一个有效子串长度的起始索引值，刚开始默认为-1,因为如果是（开始的情况计算长度还需要+1
        # indices：索引栈，即用栈的数据结构存储括号的索引值

        longest, start, indices = 0, -1, []
        for i in range(len(s)):
            if s[i] == "(":
                indices.append(i)  # 遇到左括号入栈存入索引值
            elif not indices:  # 如果索引栈里面为空，这个时候又来了一个)，则需要重新更新有效括号起始的索引值
                start = i
            elif s[i] == ")":  # 遇到右括号开始计算长度
                indices.pop()  # 先弹出最后存入的左括号的一个索引值
                if not indices:  # 如果索引栈里面为空，则
                    longest = max(longest, i - start)
                else:  # 如果索引栈不为空，则用第i个右括号的索引值减去上上一个存入的索引值
                    longest = max(longest, i - indices[-1])
        return longest


class Solution2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 思路：循环两次，从start到end相差最大的数字。此方法超时
        s_len = len(s)
        max_len = 0
        for start in range(s_len - 1):
            str_stack = []
            if s[start] == "(":
                str_stack.append("(")
                for end in range(start + 1, s_len):
                    if s[end] == "(":
                        str_stack.append("(")
                    elif s[end] == ")":
                        if str_stack:
                            str_stack.pop()
                            if not str_stack:
                                max_len = max(max_len, end - start + 1)
                        else:
                            break
            else:
                continue
        return max_len


def test_Solution2():
    s_obj = Solution2()
    assert 4 == s_obj.longestValidParentheses(")()())")


if __name__ == "__main__":
    s_obj = Solution2()
    res = s_obj.longestValidParentheses("((((((())()()()(()))(())))()))")
    print(res)
