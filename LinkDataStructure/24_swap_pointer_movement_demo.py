"""
演示：为什么 prev 只需要移动一格
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs_with_debug(head: ListNode) -> ListNode:
    """带调试信息的交换函数"""
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    step = 1
    while prev.next and prev.next.next:
        print(f"\n=== 第 {step} 次交换 ===")

        first = prev.next
        second = prev.next.next

        print(f"交换前: prev({prev.val}) -> first({first.val}) -> second({second.val})")

        # 交换
        prev.next = second
        first.next = second.next
        second.next = first

        print(f"交换后: prev({prev.val}) -> second({second.val}) -> first({first.val})")

        # 移动 prev（只移动1格）
        prev = first
        print(f"prev移动到: first({first.val})")

        if prev.next:
            print(f"下一对的first: {prev.next.val}")
            if prev.next.next:
                print(f"下一对的second: {prev.next.next.val}")

        step += 1

    return dummy.next


def print_list(head):
    """打印链表"""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))


if __name__ == "__main__":
    # 创建链表: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    print("原始链表:")
    print_list(head)

    result = swapPairs_with_debug(head)

    print("\n" + "="*50)
    print("最终结果:")
    print_list(result)

    print("\n📌 关键点:")
    print("虽然每次交换2个节点，但prev只需移动1格（移到first位置）")
    print("因为交换后，first正好是下一对的前驱节点")
