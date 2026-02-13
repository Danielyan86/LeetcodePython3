"""可视化 Floor 和 Truncate 的方向差异"""


def visualize_direction():
    """可视化两种取整方向"""

    examples = [
        (7, 2, 3.5),
        (-7, 2, -3.5),
    ]

    print("="*80)
    print("Floor Division (//) vs Truncate (int(/)) 方向对比")
    print("="*80)
    print()

    for a, b, exact in examples:
        floor = a // b
        truncate = int(a / b)

        print(f"{a} / {b} = {exact}")
        print()

        # 构建数轴
        if exact > 0:
            nums = list(range(int(floor) - 1, int(floor) + 3))
        else:
            nums = list(range(int(floor) - 1, int(truncate) + 3))

        # 数轴
        axis = "    " + "  ".join(f"{n:>3}" for n in nums)
        print(axis)

        # 精确值位置
        marker_line = "    "
        for i, n in enumerate(nums):
            if n <= exact < n + 1 or (n - 1 < exact <= n and i == 0):
                marker_line += f" {exact:>3.1f}{'':>1}"
            else:
                marker_line += "     "
        print(marker_line)

        # Floor 箭头
        floor_line = "// :"
        for n in nums:
            if n == floor:
                floor_line += "  ←■ "
            else:
                floor_line += "     "
        floor_line += f" = {floor} (向左向-∞)"
        print(floor_line)

        # Truncate 箭头
        trunc_line = "int:"
        for n in nums:
            if n == truncate:
                if exact > 0:
                    trunc_line += "  ←● "
                else:
                    trunc_line += "  ●→ "
            else:
                trunc_line += "     "
        trunc_line += f" = {truncate} (向0)"
        print(trunc_line)

        print()
        print("-" * 80)
        print()


def direction_summary():
    """总结方向规律"""
    print("="*80)
    print("方向规律总结")
    print("="*80)
    print()

    print("Floor Division (//):")
    print("  规则: 总是向左（向 -∞ 方向）")
    print("  正数结果: 向左 (3.5 → 3)")
    print("  负数结果: 向左 (-3.5 → -4)")
    print("  本质: 找小于等于结果的最大整数")
    print()

    print("Truncate (int(/)):")
    print("  规则: 总是向0")
    print("  正数结果: 向左向0 (3.5 → 3)")
    print("  负数结果: 向右向0 (-3.5 → -3)")
    print("  本质: 直接去掉小数部分")
    print()

    print("="*80)
    print("为什么 // 无法实现向0截断？")
    print("="*80)
    print()
    print("因为 // 的方向是固定的（总是向 -∞），")
    print("而向0截断需要「根据正负改变方向」：")
    print("  - 正数时向左（向0）")
    print("  - 负数时向右（向0）")
    print()
    print("所以 Python 必须用 int(a / b) 来实现向0截断！")
    print("="*80)


if __name__ == "__main__":
    visualize_direction()
    direction_summary()
