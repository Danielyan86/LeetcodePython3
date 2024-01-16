# 思路，两个指针倒着遍历两个字符串  和88有点类似
# 关键-如果一个指针《0了，则这个数字直接取0，相当于在前面补0，让两个数字长度一样
# 注意carry，digital的位置顺序
# 注意res每次叠加顺序
# 最后完了记得判断carry，是否需要补一个1
# https://leetcode.cn/problems/add-strings/description/
# https://leetcode.cn/problems/merge-sorted-array/submissions/495464149/  （88）
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        p1, p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        while p1 >= 0 or p2 >= 0:
            n1 = int(num1[p1]) if p1 >= 0 else 0
            n2 = int(num2[p2]) if p2 >= 0 else 0
            carry, digit = divmod(n1 + n2 + carry, 10)
            res = str(digit) + res
            p1, p2 = p1 - 1, p2 - 1
        return "1" + res if carry else res
