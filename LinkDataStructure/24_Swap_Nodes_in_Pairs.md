# 24. Swap Nodes in Pairs

## 题目描述

给定一个链表，交换每两个相邻的节点，并返回其头部。你必须在不修改节点值的情况下解决问题（即只能改变节点本身）。

**难度**: Medium

## 示例

### 示例 1:
```
输入: head = [1,2,3,4]
输出: [2,1,4,3]

原链表: 1 -> 2 -> 3 -> 4
结果:   2 -> 1 -> 4 -> 3
```

### 示例 2:
```
输入: head = []
输出: []
```

### 示例 3:
```
输入: head = [1]
输出: [1]
```

## 解题思路

### 方法一：迭代法 ⭐️ 推荐

# 思路并不复杂，但是实际处理交换时候还是有点绕。 需要注意这么几点
# 每次需要往后判断两个节点，因为实际是跳两个格子后交换
# 添加两个临时变量存储节点，这样比较方便，用更多空间增加可读性
# 具体交换时候搞清楚顺序，什么操作是移动指针，什么操作是简历链接
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        dummy = ListNode(val=0, next=head)
        pre = dummy
        while pre.next and pre.next.next:
            cur, nt = pre.next, pre.next.next
            cur.next = nt.next
            pre.next = nt
            nt.next = cur
            pre =cur

        return dummy.next