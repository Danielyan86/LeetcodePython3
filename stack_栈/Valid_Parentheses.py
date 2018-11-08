""" 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_list = []
        for letter in s:
            if letter in '({[':
                p_list.append(letter)
            else:
                if p_list:
                    if letter == ')':
                        if p_list.pop() != '(':
                            return False
                    elif letter == ']':
                        if p_list.pop() != '[':
                            return False
                    elif letter == '}':
                        if p_list.pop() != '{':
                            return False
                else:
                    return False
        return False if p_list else True


if __name__ == '__main__':
    parenthesis = "{[]}"
    s_obj = Solution()
    res = s_obj.isValid(parenthesis)
    print(res)
