# two pointers
# 注意是判断当前指针存在与否，而不是next
# 注意A或者B指针走到头之后是 重新指向另外一个链表的头节点，而不是另外一个指针！
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA, pointerB = headA, headB
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        # At this point, either pointers have met at the intersection or both are None
        return pointerA


# use set data structure
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_set = set()
        a, b = headA, headB
        while a:
            a_set.add(a)
            a = a.next
        while b:
            if b in a_set:
                return b
            b = b.next
