# 这道题的问题在于要理解加法顺序，平时我们是从左往右写数字，也就是高位在左边，但是具体计算的时候是从右往左计算
# 因此左边是低位，刚好符合计算习惯，不用逆向遍历
# 需要注意处理位数对不齐的情况
# 加法计算需要处理进位情况 可以直接使用divmod函数
# 主要注意返回是一个list node，不是一个整数！搞清楚节点的挂载和赋值

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
