class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Initialize the heap with the first node from each list
        # for i, lst in enumerate(lists):
        #     if lst:
        #         heapq.heappush(min_heap, (lst.val, lst))

        # 为什么一定要传入一个i, 因为第三个lst是一个object，如果lst.val 相同则第三个没法比较，从而出错
        # 所以i其实完全没有参与逻辑，只是为了让heap 排序不出错
        for i, node in enumerate(lists):
            if node:  #  可能是一个None的 list [None]
                heapq.heappush(node_lst, (node.val, i, node))
        # Dummy node to simplify the result list construction
        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next

            # Move to the next node in the list from which the last node was taken
            # 弹出了一个元素的链表继续push下一个node到队列
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next
