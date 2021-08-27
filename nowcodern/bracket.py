class Solution:
    def isValid(self, s):
        bracket_stack = []
        for char in s:
            if char in "({[":
                bracket_stack.append(char)
            else:
                if bracket_stack:
                    last_char = bracket_stack.pop()
                    new_str = last_char + char
                    if new_str in ["()", "[]", "{}"]:
                        continue
                    else:
                        return False
                else:
                    return False
        return True if not bracket_stack else False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{"))
    print(s.isValid("{}"))
    print(s.isValid("{]"))
    print(s.isValid("}"))
    print(s.isValid("{[()]}"))
    print(s.isValid("{}()[]"))
