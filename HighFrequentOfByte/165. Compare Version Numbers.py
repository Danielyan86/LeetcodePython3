# 逗号分割，转化成数字list
# 取最大长度为比较长度
# 从左往右取下标依次比较
# 当下标超出任意一个数组最大值时候取0比较
# 如果不想等则提前结束
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split(".")]
        v2 = [int(x) for x in version2.split(".")]
        max_l = max(len(v1), len(v2))
        for i in range(max_l):
            n1 = 0 if i >= len(v1) else v1[i]
            n2 = 0 if i >= len(v2) else v2[i]
            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        return 0
