from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        else:
            # 代码可以再简化
            p1, p2 = list1, list2
            head, p3 = None, None
            if p1.val <= p2.val:
                head = p3 = p1
                p1 = p1.next
            else:
                head = p3 = p2
                p2 = p2.next
            p3.next = None
            while p1 and p2:
                if p1.val <= p2.val:
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
                p3 = p3.next
        # 注意最后一个边界条件
        p3.next = p1 if p1 else p2
        return head


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        if l1 is None and l2 is None:
            return None
        if l1 is None and l2:
            return l2
        if l1 and l2 is None:
            return l1
        if l1.val <= l2.val:
            l3 = l1
            l1 = l1.next
        else:
            l3 = l2
            l2 = l2.next
        pre = l3
        # 只能是两个都存在，不然没法比较，而且剩下元素本身也有顺序
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                pre = pre.next  # 注意previous的指针移动
                l1 = l1.next
            else:
                pre.next = l2
                pre = pre.next
                l2 = l2.next
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2

        return l3


def convert_list_to_nodes(num_list):
    head = ListNode(num_list[0])
    cur = head
    for num in num_list[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


def traversal_node_list(node):
    while node:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    a = [1, 2, 4]
    b = [1, 3, 4]
    a_node_list = convert_list_to_nodes(a)
    b_node_list = convert_list_to_nodes(b)
    s = Solution2()
    ans = s.mergeTwoLists(a_node_list, b_node_list)
