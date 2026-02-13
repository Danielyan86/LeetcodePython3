"""演示 // 的本意：floor division（向下取整）"""

import math


def demo_floor_division():
    """Floor division 的含义"""
    print("="*80)
    print("Floor Division (//) 的本意：向下取整到最接近的整数")
    print("="*80)
    print()

    examples = [
        (7, 2),
        (8, 3),
        (-7, 2),
        (-8, 3),
        (7, -2),
        (-7, -2),
    ]

    print(f"{'a':<6} {'b':<6} {'a/b':<12} {'floor(a/b)':<15} {'a//b':<10} {'验证'}")
    print("-" * 80)

    for a, b in examples:
        true_div = a / b
        floor_result = math.floor(a / b)
        floor_div = a // b
        match = "✓" if floor_result == floor_div else "✗"

        print(f"{a:<6} {b:<6} {true_div:<12.3f} {floor_result:<15} {floor_div:<10} {match}")

    print("\n" + "="*80)
    print("结论: a // b == math.floor(a / b)")
    print("="*80)


def visual_explanation():
    """可视化解释"""
    print("\n\n可视化理解：Floor Division 总是向下取整（向 -∞ 方向）\n")

    examples = [
        (7, 2, "正数"),
        (-7, 2, "负数"),
    ]

    for a, b, desc in examples:
        result = a / b
        floor = a // b
        print(f"{desc}: {a} / {b} = {result}")
        print(f"数轴: ... {floor-2}  {floor-1}  [{floor}]  {floor+1}  {floor+2} ...")
        print(f"      {result:.2f} 在这里 ↑")
        print(f"      向下取整到 {floor}")
        print()


def use_cases():
    """// 的实际应用场景"""
    print("\n" + "="*80)
    print("// (Floor Division) 的典型应用场景")
    print("="*80)
    print()

    # 场景1：数组索引计算
    print("1. 数组索引/分页计算")
    total_items = 100
    page_size = 15
    num_pages = total_items // page_size + (1 if total_items % page_size else 0)
    print(f"   100个元素，每页15个 → 需要 {num_pages} 页")
    print(f"   第50个元素在第 {50 // page_size + 1} 页")
    print()

    # 场景2：二分查找
    print("2. 二分查找中点")
    left, right = 0, 10
    mid = (left + right) // 2
    print(f"   left={left}, right={right} → mid={mid}")
    print()

    # 场景3：坐标转换
    print("3. 坐标转换（1D → 2D）")
    index = 23
    cols = 5
    row = index // cols
    col = index % cols
    print(f"   1D索引 {index} → 2D坐标 ({row}, {col})")
    print()

    # 场景4：时间计算
    print("4. 时间单位转换")
    seconds = 3725
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    print(f"   {seconds}秒 = {hours}小时 {minutes}分 {secs}秒")
    print()


def why_not_truncate():
    """为什么不用 truncate？"""
    print("\n" + "="*80)
    print("为什么 Python 选择 Floor Division 而不是 Truncate？")
    print("="*80)
    print()

    print("原因：Floor Division 有更好的数学性质")
    print()

    # 性质1：除法和模运算的关系保持一致
    print("1. 保持除法定理: a = (a // b) * b + (a % b)")
    for a, b in [(7, 3), (-7, 3)]:
        quotient = a // b
        remainder = a % b
        verify = quotient * b + remainder
        print(f"   {a} = ({a} // {b}) * {b} + ({a} % {b})")
        print(f"   {a} = {quotient} * {b} + {remainder} = {verify} ✓")
    print()

    print("2. 如果用 truncate，负数的模运算会变得混乱")
    print("   Floor: -7 // 3 = -3, -7 % 3 = 2  → -3*3 + 2 = -7 ✓")
    print("   Truncate: int(-7/3) = -2, 但 -2*3 + ? = -7 → 余数变成 -1")
    print()

    print("3. Floor division 在数组索引中更自然")
    print("   例如：月份 0-11，计算季度")
    for month in [0, 1, 2, 3]:
        quarter = month // 3
        print(f"   月份 {month} → 第 {quarter} 季度")
    print()


if __name__ == "__main__":
    demo_floor_division()
    visual_explanation()
    use_cases()
    why_not_truncate()

    print("\n" + "="*80)
    print("总结")
    print("="*80)
    print("// 的本意: Floor Division (向下取整)")
    print("  - 定义: a // b == math.floor(a / b)")
    print("  - 特点: 总是向 -∞ 方向取整")
    print("  - 优势: 保持除法定理，模运算一致")
    print()
    print("LeetCode 227 要求 truncate (向零取整):")
    print("  - 应该用: int(a / b)")
    print("  - 不能用: a // b")
    print("="*80)
