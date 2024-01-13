# 为什么一定要传入一个i, 因为第三个lst是一个object，如果lst.val 相同则第三个没法比较，从而出错
# 所以i其实完全没有参与逻辑，只是为了让heap 排序不出错

# Move to the next node in the list from which the last node was taken
# 弹出了一个元素的链表继续push下一个node到队列


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        min_heapq = []
        for i, node in enumerate(lists):
            if node:  # 首节点可能为空
                heapq.heappush(min_heapq, (node.val, i, node))
        dummy_h = ListNode()
        cur = dummy_h
        while min_heapq:
            val, i, node = heapq.heappop(min_heapq)
            cur.next = node
            cur = cur.next
            tmp = cur.next
            if tmp:  # 下一个节点如果存在，则继续push
                heapq.heappush(min_heapq, (tmp.val, i, tmp))
        return dummy_h.next
