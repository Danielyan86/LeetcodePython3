"""测试修正前后的差异"""


class SolutionOriginal:
    """原始代码（有问题）"""
    def calculate(self, s: str) -> int:
        res, prev = 0, 0
        num = 0
        sign = '+'
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            if not c: continue  # 问题1: 无法跳过空格

            if sign == '+':
                res += prev
                prev = num
            elif sign == '-':
                res += prev
                prev = -num
            elif sign == '*':
                prev = prev * num
            elif sign == '/':
                prev = int(prev // num)  # 问题2: 除法错误

            sign = c
            num = 0

        return res + prev


class SolutionFixed:
    """修正后的代码"""
    def calculate(self, s: str) -> int:
        res, prev = 0, 0
        num = 0
        sign = '+'
        for c in s + '+':
            if c.isdigit():
                num = num * 10 + int(c)
                continue

            if c == ' ': continue  # 修复1: 正确跳过空格

            if sign == '+':
                res += prev
                prev = num
            elif sign == '-':
                res += prev
                prev = -num
            elif sign == '*':
                prev = prev * num
            elif sign == '/':
                prev = int(prev / num)  # 修复2: 使用 / 而不是 //

            sign = c
            num = 0

        return res + prev


def test():
    sol_orig = SolutionOriginal()
    sol_fixed = SolutionFixed()

    test_cases = [
        (" 3/2 ", 1),           # 测试空格
        ("5-7/2", 2),           # 测试负数除法: 5 - int(-7/2) = 5 - (-3) = 5 - 3 = 2
        ("3+2*2", 7),
        ("14-3/2", 13),
    ]

    print("测试结果对比:\n")
    for s, expected in test_cases:
        orig = sol_orig.calculate(s)
        fixed = sol_fixed.calculate(s)

        orig_status = "✓" if orig == expected else "✗"
        fixed_status = "✓" if fixed == expected else "✗"

        print(f"输入: '{s}'")
        print(f"  期望: {expected}")
        print(f"  原始代码: {orig} {orig_status}")
        print(f"  修正代码: {fixed} {fixed_status}")
        print()


if __name__ == "__main__":
    test()
