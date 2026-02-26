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

### 核心要点

1.注意是否继续遍历的判定条件，每次需要往后判断两个节点
2. 注意两个节点教会时候的具体顺序，借助图形化思考
3. 每次节点往后移动两个节点
4. 重置当前节点往后的两个节点
5. 

### 代码实现

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归终止条件
        if not head or not head.next:
            return head

        # 保存第二个节点
        second = head.next

        # 递归处理后续部分，并连接到第一个节点
        head.next = self.swapPairs(second.next)

        # 交换：让第二个节点指向第一个
        second.next = head

        # 返回新的头节点（原来的第二个节点）
        return second
```

### 复杂度分析

- **时间复杂度**: O(n)
- **空间复杂度**: O(n) - 递归调用栈深度

## 相关题目

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - 反转链表基础
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - 本题的进阶版，每 k 个一组反转
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) - 反转部分链表

## 标签

`Linked List` `Recursion` `Two Pointers`
