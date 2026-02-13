"""演示 int(a/b) 和 a//b 的区别"""


def test_division():
    """对比两种除法"""

    test_cases = [
        (7, 2, "正数"),
        (-7, 2, "负数除以正数"),
        (7, -2, "正数除以负数"),
        (-7, -2, "负数除以负数"),
        (-1, 2, "小负数"),
        (-8, 3, "不能整除的负数"),
    ]

    print("对比 int(a/b) 和 a//b:\n")
    print(f"{'a':<5} {'b':<5} {'a/b':<10} {'int(a/b)':<12} {'a//b':<12} {'相同?':<8} {'说明'}")
    print("-" * 80)

    for a, b, desc in test_cases:
        true_div = a / b
        truncate = int(a / b)
        floor_div = a // b
        same = "✓" if truncate == floor_div else "✗"

        print(f"{a:<5} {b:<5} {true_div:<10.2f} {truncate:<12} {floor_div:<12} {same:<8} {desc}")

    print("\n" + "="*80)
    print("结论：")
    print("  int(a/b): 向零截断 - 结果总是更接近 0")
    print("  a//b:     向下取整 - 结果总是更小（向 -∞ 方向）")
    print("  负数时两者不同！LeetCode 227 要求向零截断，所以用 int(a/b)")
    print("="*80)


def calculator_example():
    """实际题目中的差异"""
    print("\n\n实际题目示例: '5-7/2'")
    print("-" * 40)

    # 使用 int(/) - 正确
    result_correct = 0
    last_correct = 0
    # 5
    result_correct += last_correct
    last_correct = 5
    # -7
    result_correct += last_correct  # 5
    last_correct = -7
    # /2
    last_correct = int(last_correct / 2)  # int(-7/2) = int(-3.5) = -3
    result_correct += last_correct  # 5 + (-3) = 2

    print(f"使用 int(last / num): 5 - int(-7/2) = 5 - (-3) = 5 - 3 = {result_correct} ✓")

    # 使用 // - 错误
    result_wrong = 0
    last_wrong = 0
    # 5
    result_wrong += last_wrong
    last_wrong = 5
    # -7
    result_wrong += last_wrong  # 5
    last_wrong = -7
    # //2
    last_wrong = last_wrong // 2  # -7 // 2 = -4
    result_wrong += last_wrong  # 5 + (-4) = 1

    print(f"使用 last // num:      5 - (-7//2) = 5 - (-4) = 5 - 4 = {result_wrong} ✗")

    print(f"\n期望结果: 2")
    print(f"正确性: int(/) {'✓' if result_correct == 2 else '✗'}, // {'✓' if result_wrong == 2 else '✗'}")


if __name__ == "__main__":
    test_division()
    calculator_example()
