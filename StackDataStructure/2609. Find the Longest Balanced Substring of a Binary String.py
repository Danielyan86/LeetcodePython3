# 和括号题不太一样，不太适合用stack解决
#  考虑各种边界条件
# 考虑计数出发条件和算法，
# 0必须在1前面，如果是连续的000+11，只用取小的个数再*2，
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        max_l = 0
        pre, cur = None, 0
        num_dic = {"0": 0, "1": 0}
        for i in range(n):
            if i == 0 and s[i] == "0":
                num_dic["0"] += 1
            else:
                if s[i] == "0" and s[i - 1] == "0":
                    num_dic["0"] += 1
                if s[i] == "0" and s[i - 1] == "1":
                    # 触发计数
                    max_l = max(max_l, min(num_dic["0"], num_dic["1"]) * 2)
                    num_dic = {"0": 1, "1": 0}
                if s[i] == "1" and num_dic["0"] != 0:
                    num_dic["1"] += 1
        max_l = max(max_l, min(num_dic["0"], num_dic["1"]) * 2)
        return max_l
