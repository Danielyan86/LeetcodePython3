# Given the head of a linked list, remove the nth node from the end of the list and return its head.

## 核心思路：距离差思维 🎯

**本质：简单的数学问题 —— 快慢指针始终保持固定距离差 n**

### 为什么单指针不行？

单指针扫一遍无法定位倒数第 n 个节点，因为不知道链表总长度。

### 双指针解法

1. **建立距离差**：快指针先走 n 步 → 快慢指针相差 n 个节点
2. **保持距离差**：快慢指针同步移动 → 距离差始终 = n
3. **利用距离差**：快指针到末尾时 → 慢指针自然在倒数第 n 个位置

### 数学本质

```
链表总长度 = L
快指针走的距离 = L
慢指针走的距离 = L - n
慢指针距离右边(末尾) = L - (L - n) = n
```

**换个视角理解：**
- 快指针抢跑 n 步 = 相当于从右边倒数 n 步的位置被锁定
- 当快指针走完整个链表时，慢指针刚好在"距离右边 n 步"的位置
- 不需要"倒着数"，只需维持固定距离差即可！

```
示例：删除倒数第 2 个节点

步骤1：快指针先走 n+1 步（使用 dummy 节点）
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
slow     fast(走3步)
         距离差 = 3

步骤2：同步移动，距离差保持不变
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
              slow          fast
              距离差 = 3（不变）

步骤3：fast 到 null，slow.next 就是要删除的节点
              slow               fast
               ↓                  ↓
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> null
                    ↑
              slow.next（倒数第2个）
```


```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 使用 dummy 节点处理边界情况（如删除头节点）
        dummy = ListNode(0, head)
        fast = slow = dummy

        # 阶段1：建立距离差 n+1
        # fast 先走 n+1 步，使 slow 定位到要删除节点的前一个位置
        for _ in range(n + 1):
            fast = fast.next

        # 阶段2：保持距离差，同步移动
        # 当 fast 到达 null 时，slow 刚好在目标节点之前
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除节点：跳过 slow.next
        slow.next = slow.next.next
        return dummy.next
```

## 复杂度分析

- **时间复杂度**：O(L)，L 为链表长度，只遍历一次
- **空间复杂度**：O(1)，只用了两个指针

## 关键技巧

1. **dummy 节点**：处理删除头节点的边界情况
2. **n+1 步**：让 slow 停在要删除节点的**前一个**位置，方便删除
3. **距离差**：核心是维持固定距离，而不是倒着计数

## 多角度理解

```text
角度1 - 距离差：快慢指针距离始终 = n
角度2 - 数学公式：慢指针距离右边 = L - (L - n) = n
角度3 - 倒推视角：快指针抢跑 n = 从右边往左锁定位置
```
