"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# 此题关键点在于理解hash key的map关系是原有addressmap到新的address
class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return
        if head.next is None:
            return copy.deepcopy(head)

        cur = head.next
        h2 = cur2 = copy.deepcopy(head)
        dic = {head: cur2}
        # initilize the dic to build the node map realatiionship
        # key is old node address, value is the new node address,this is the key point
        while cur:
            cur2.next = dic[cur] = Node(cur.val)
            cur = cur.next
            cur2 = cur2.next
        cur = head
        while cur:
            if cur.random is None:
                dic[cur].random = None
            else:
                dic[cur].random = dic[cur.random]
            cur = cur.next

        return h2
