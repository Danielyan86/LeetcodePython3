class Solution:
    def evalRPN(self, tokens: list):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 更少的代码，不过使用eval效率低
        num_stack = []
        for item in tokens:
            if item not in "+-*/":
                num_stack.append(item)
            else:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                res = eval("{0}{1}{2}".format(num2, item, num1))
                num_stack.append(int(res))
        return int(num_stack[0])


class Solution2:
    def evalRPN(self, tokens: list):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        for item in tokens:
            if item not in "+-*/":
                num_stack.append(int(item))
            else:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                if item == "+":
                    res = num2 + num1
                elif item == "-":
                    res = num2 - num1
                elif item == "*":
                    res = num2 * num1
                elif item == "/":
                    res = int(num2 / num1)
                num_stack.append(res)
        return num_stack[0]


def test_evalRPN():
    solution = Solution2()
    assert 9 == solution.evalRPN(["2", "1", "+", "3", "*"])
    assert 6 == solution.evalRPN(["4", "13", "5", "/", "+"])
    assert 22 == solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    assert 18 == solution.evalRPN(["18"])


if __name__ == '__main__':
    solution = Solution2()
    res = solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(res)
