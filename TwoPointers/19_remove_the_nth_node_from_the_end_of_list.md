# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# 这题刚一看会发现个问题，因为是删除倒数第n个节点，所以用一个指针扫一遍是完不成的
# 这里巧妙应用双指针打法，是因为有个隐含条件，当一个指针走了n步，那么剩下就是 X
# 快慢指针最佳理解方式，不要看成倒着数第N个，把链表看成一个+n延长线，当快指针抢跑n之后，相当于把多出来的N已经跑了，这个时候慢指针再出发，当快指针把原有x跑完时候，，慢指针刚好到差N的地方，因为快指针抢跑了n步


```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # fast 先走 n+1 步
        for _ in range(n + 1):
            fast = fast.next
        
        # 同时移动直到 fast 为 null
        while fast:
            fast = fast.next
            slow = slow.next
        
        # 删除节点
        slow.next = slow.next.next
        return dummy.next
```