"""
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
- The number of nodes in the list is in the range [0, 100].
- 0 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代法：使用虚拟头节点，逐对交换节点

        时间复杂度: O(n) - 遍历一次链表
        空间复杂度: O(1) - 只用了常数个指针
        """
        # 创建虚拟头节点，简化边界处理
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 当存在待交换的两个节点时继续循环
        while prev.next and prev.next.next:
            # 标识待交换的两个节点
            first = prev.next
            second = prev.next.next

            # 执行交换：prev -> first -> second -> next
            # 变为：prev -> second -> first -> next
            prev.next = second           # prev指向second
            first.next = second.next     # first指向second的下一个
            second.next = first          # second指向first

            # 移动prev到下一对的前驱位置
            prev = first

        return dummy.next

    def swapPairs_recursive(self, head: ListNode) -> ListNode:
        """
        递归法：递归处理后续节点，然后交换当前两个节点

        时间复杂度: O(n)
        空间复杂度: O(n) - 递归调用栈
        """
        # Base case: 如果链表为空或只有一个节点，无需交换
        if not head or not head.next:
            return head

        # 保存第二个节点
        second = head.next

        # 递归处理后续节点，返回新的头节点
        # head.next应该指向递归处理后的结果
        head.next = self.swapPairs_recursive(second.next)

        # 交换：让second指向head
        second.next = head

        # 返回新的头节点（原来的第二个节点）
        return second


def create_linked_list(values):
    """辅助函数：从列表创建链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """辅助函数：将链表转换为列表用于打印"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4])
    result1 = solution.swapPairs(head1)
    print(f"Input: [1,2,3,4]")
    print(f"Output: {linked_list_to_list(result1)}")  # [2,1,4,3]

    # Test case 2
    head2 = create_linked_list([])
    result2 = solution.swapPairs(head2)
    print(f"\nInput: []")
    print(f"Output: {linked_list_to_list(result2)}")  # []

    # Test case 3
    head3 = create_linked_list([1])
    result3 = solution.swapPairs(head3)
    print(f"\nInput: [1]")
    print(f"Output: {linked_list_to_list(result3)}")  # [1]

    # Test case 4: 递归方法
    head4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = solution.swapPairs_recursive(head4)
    print(f"\nInput: [1,2,3,4,5] (Recursive)")
    print(f"Output: {linked_list_to_list(result4)}")  # [2,1,4,3,5]
