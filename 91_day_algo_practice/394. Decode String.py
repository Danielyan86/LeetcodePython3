class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        cur_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack.append((current_num, cur_str))
                current_num = 0
                cur_str = ""
            elif char == "]":
                num, prev_str = stack.pop()
                cur_str = prev_str + num * cur_str
            else:
                cur_str += char

        return cur_str
