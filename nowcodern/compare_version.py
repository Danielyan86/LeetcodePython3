class Solution:
    def compare(self, version1, version2):
        ver_num_list1, ver_num_list2 = version1.split("."), version2.split(".")
        ver_num_list1 = [int(n) for n in ver_num_list1]
        ver_num_list2 = [int(n) for n in ver_num_list2]
        while ver_num_list1[-1] ==0:
            ver_num_list1.pop()
        while ver_num_list2[-1] == 0:
            ver_num_list2.pop()
        if ver_num_list1 == ver_num_list2:
            return 0
        for n in range(0, min(len(ver_num_list1), len(ver_num_list2))):
            if ver_num_list1[n] > ver_num_list2[n]:
                return 1
            elif ver_num_list1[n] < ver_num_list2[n]:
                return -1
        if len(ver_num_list1) > len(ver_num_list2):
            return 1
        if len(ver_num_list1) < len(ver_num_list2):
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.compare("1.1", "2.1"))
    print(s.compare("1.1", "1.01"))
    print(s.compare("1.1", "1.1.1"))
    print(s.compare("2.0.1", "2"))
    print(s.compare("0.226", "0.36"))
    print(s.compare("1.0", "1.0.0"))
