"""
可视化演示：prev 如何"自动跑到后一个"
"""


def visualize_swap():
    print("=" * 60)
    print("可视化演示：prev 的自动移动")
    print("=" * 60)

    print("\n【第1次交换】")
    print("交换前:")
    print("  dummy -> [1 -> 2] -> [3 -> 4]")
    print("   prev    └─当前对─┘   └─下一对─┘")
    print("           first second")

    print("\n交换操作后:")
    print("  dummy -> [2 -> 1] -> [3 -> 4]")
    print("   prev         first  └─下一对─┘")
    print("                ↑")
    print("           自动变成下一对的前驱！")

    print("\n执行 prev = first:")
    print("  dummy -> 2 -> [1 -> 3 -> 4]")
    print("                prev └─下一对─┘")
    print("                      first second")

    print("\n" + "─" * 60)

    print("\n【第2次交换】")
    print("交换前:")
    print("  dummy -> 2 -> 1 -> [3 -> 4]")
    print("                prev  └─当前对─┘")
    print("                      first second")

    print("\n交换操作后:")
    print("  dummy -> 2 -> 1 -> [4 -> 3]")
    print("                prev       first")
    print("                           ↑")
    print("                      又自动到位了！")

    print("\n执行 prev = first:")
    print("  dummy -> 2 -> 1 -> 4 -> 3")
    print("                          prev")
    print("                          (没有下一对了，结束)")

    print("\n" + "=" * 60)
    print("💡 精髓：")
    print("   交换后，原来的 first 位置刚好是下一对的前驱")
    print("   所以只需要 prev = first，就自动移到了正确位置")
    print("=" * 60)


def demonstrate_with_positions():
    print("\n\n📍 位置编号演示：")
    print("=" * 60)

    print("\n原始链表（标注位置）:")
    print("  位置:  0     1     2     3     4")
    print("       dummy -> 1 -> 2 -> 3 -> 4")

    print("\n第1次交换:")
    print("  prev在位置0，交换位置1和2")
    print("  交换后: dummy -> 2 -> 1 -> 3 -> 4")
    print("  prev移动到位置2（原first的位置）")

    print("\n第2次交换:")
    print("  prev在位置2，交换位置3和4")
    print("  交换后: dummy -> 2 -> 1 -> 4 -> 3")
    print("  prev移动到位置4（原first的位置）")

    print("\n结论：")
    print("  ✅ 每次交换2个节点")
    print("  ✅ prev移动1个位置（到原first）")
    print("  ✅ 处理完所有的对")


if __name__ == "__main__":
    visualize_swap()
    demonstrate_with_positions()
