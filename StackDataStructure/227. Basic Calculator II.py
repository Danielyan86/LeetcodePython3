"""
227. Basic Calculator II
Medium

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be
in the range of [-2^31, 2^31 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as
mathematical expressions, such as eval().

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1

Example 3:
Input: s = " 3+5 / 2 "
Output: 5

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
- s represents a valid expression.
- All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
- The answer is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def calculate(self, s: str) -> int:
        """
        Simple approach without stack - just track last number and running total.

        Key insight:
        - Keep a running result and track the last number
        - For +/-: add last to result, update last with current num
        - For */: directly update last (no need to touch result yet)
        - Finally add last to result

        Trick: Add a sentinel '+' at the end to ensure the last number is processed

        Example: "3+2*2"
        - See 3: last=3
        - See +: result=0+3=3, ready for next
        - See 2: last=2
        - See *: keep result=3, just update last
        - See 2: last=2*2=4
        - See '+' (sentinel): result=3+4=7

        Time: O(n) where n is length of string
        Space: O(1) - only use constant extra space
        """

        class Solution:
            def calculate(self, s: str) -> int:
                result, last, num = 0, 0, 0
                operator_pre = "+"

                for char in s + "+":  # Add sentinel to ensure last number is processed
                    if char.isdigit():
                        num = num * 10 + int(char)
                        continue

                    if char == " ":  # Skip spaces
                        continue

                    # Process the previous operator with current num
                    if operator_pre == "+":
                        result += last  # Add previous number to result
                        last = num  # Store current number
                    elif operator_pre == "-":
                        result += last
                        last = -num  # Store as negative
                    elif operator_pre == "*":
                        last = last * num  # Multiply with last number
                    elif operator_pre == "/":
                        last = int(last / num)  # Truncate toward zero (not //)

                    operator_pre = char  # Update operator for next iteration
                    num = 0  # Reset num

                return result + last

        class SolutionWithStack:
            def calculate(self, s: str) -> int:
                """
                Alternative: Stack-based approach (less space efficient but more intuitive for some).

                Store all numbers in stack, handling * and / immediately.
                Finally sum all numbers in stack.

                Time: O(n)
                Space: O(n) for the stack
                """
                if not s:
                    return 0

                stack = []
                num = 0
                operator = "+"

                for i, char in enumerate(s):
                    if char.isdigit():
                        num = num * 10 + int(char)

                    # Process when we hit an operator or reach the end
                    # Skip spaces unless it's the last character
                    if char != " " and not char.isdigit() or i == len(s) - 1:
                        if operator == "+":
                            stack.append(num)
                        elif operator == "-":
                            stack.append(-num)
                        elif operator == "*":
                            stack.append(stack.pop() * num)
                        elif operator == "/":
                            stack.append(int(stack.pop() / num))

                        if i < len(s) - 1:  # Don't update operator on last char
                            operator = char
                        num = 0

                return sum(stack)


def test_calculator():
    """Test cases for Basic Calculator II"""
    sol = Solution()
    sol_stack = SolutionWithStack()

    test_cases = [
        ("3+2*2", 7),
        (" 3/2 ", 1),
        (" 3+5 / 2 ", 5),
        ("42", 42),
        ("1-1+1", 1),
        ("2*3*4", 24),
        ("100/2/5", 10),
        ("14-3/2", 13),  # 14 - 1 = 13
        ("5-7/2", 2),  # 5 - int(-7/2) = 5 - (-3) = 5 - 3 = 2 (test truncate toward zero)
        ("1*2-3/4+5*6-7*8+9/10", -24),  # Complex expression
    ]

    for s, expected in test_cases:
        result1 = sol.calculate(s)
        result2 = sol_stack.calculate(s)

        assert result1 == expected, f"Solution failed for '{s}': got {result1}, expected {expected}"
        assert result2 == expected, f"SolutionWithStack failed for '{s}': got {result2}, expected {expected}"

        print(f"✓ Test passed: '{s}' = {result1}")

    print("\nAll tests passed!")


if __name__ == "__main__":
    test_calculator()
