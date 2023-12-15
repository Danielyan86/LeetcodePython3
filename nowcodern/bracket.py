# 判断长度
# 设置空list
# 先左后右
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        st = []
        for ch in s:
            if ch in "([{":
                st.append(ch)
            else:
                # if not st: return False
                if not st:
                    return False
                if st.pop() + ch not in "(){}[]":
                    return False
        return False if st else True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{"))
    print(s.isValid("{}"))
    print(s.isValid("{]"))
    print(s.isValid("}"))
    print(s.isValid("{[()]}"))
    print(s.isValid("{}()[]"))
