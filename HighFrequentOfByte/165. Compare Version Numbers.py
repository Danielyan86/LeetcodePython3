# 逗号分割，转化成数字list
# 根据长度补0
# 取下标依次比较
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lst1 = [int(x) for x in version1.split(".")]
        lst2 = [int(x) for x in version2.split(".")]

        while len(lst1) < len(lst2):
            lst1.append(0)
        while len(lst2) < len(lst1):
            lst2.append(0)
        i = 0
        while i < len(lst1):
            if lst1[i] > lst2[i]:
                return 1
            elif lst1[i] < lst2[i]:
                return -1
            i += 1
        return 0
