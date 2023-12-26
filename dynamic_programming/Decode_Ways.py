class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_list = [int(item) for item in list(s)]
        s_len = len(s)
        if num_list[0] == 0:
            return 0
        if s_len == 1:
            return 1
        elif s_len >= 2:
            a = 1
            if int(num_list[0] * 10 + num_list[1]) <= 26:
                if num_list[1] == 0:
                    b = 1
                else:
                    b = 2
            else:
                if num_list[1] == 0:
                    b = 0
                else:
                    b = 1
            if s_len == 2:
                return b
            for i in range(s_len - 2):
                if num_list[i + 2] == 0 and num_list[i + 1] * 10 + num_list[i + 2] > 26:
                    return 0
                if num_list[i + 2] == 0:
                    if num_list[i + 1] == 0:
                        return 0
                    if num_list[i + 1]:
                        a, b = b, a
                elif num_list[i + 1] * 10 + num_list[i + 2] > 26:
                    a, b = b, b
                else:
                    if num_list[i + 1] == 0:
                        if num_list[i] * 10 > 26:
                            return 0
                        else:
                            a, b = b, a
                    else:
                        a, b = b, a + b
        return b


def test_Solution():
    s_obj = Solution()
    assert 3 == s_obj.numDecodings("226")
    assert 2 == s_obj.numDecodings("12")
    assert 0 == s_obj.numDecodings("990")
    assert 1 == s_obj.numDecodings("27")
    assert 0 == s_obj.numDecodings("100")
    assert 1 == s_obj.numDecodings("101")
    assert 0 == s_obj.numDecodings("301")


if __name__ == "__main__":
    s = "301"
    s_obj = Solution()
    res = s_obj.numDecodings(s)
    print(res)
