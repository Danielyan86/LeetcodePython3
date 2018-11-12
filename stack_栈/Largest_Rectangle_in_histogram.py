# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        max_area = 0
        for index in range(len(heights)):
            while heights[index] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = index - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(index)
        heights.pop()
        return max_area

    def _increase_list(self, heights: list) -> int:
        # [1, 3, 4, 7]
        stack_index = [index for index in range(len(heights))]
        max_area = 0
        top_index = len(stack_index)
        while stack_index:
            index = stack_index.pop()
            width = top_index - index
            area = heights[index] * width
            print(area)
            max_area = max(max_area, area)
        return max_area


class Solution2:
    def largestRectangleArea(self, heights: list) -> int:
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)  # 末尾添加一个-1，方便我们用索引值相减，求出长方形的宽。假设最后一个柱子为最大的单个柱子,索引值为index，则宽度为len(height)-index
        max_area = 0
        stack_index = []
        # 索引值入栈
        index = 0
        while index < len(heights):
            if stack_index:  # 如果不为空，判断是否升序，如果升序，则入栈
                if heights[index] >= heights[stack_index[-1]]:
                    stack_index.append(index)
                    index = index + 1
                else:  # 否则开始计算，直到升序
                    previous_index = stack_index.pop()
                    if stack_index:
                        max_area = max(max_area, (index - stack_index[-1] - 1) * heights[previous_index])
                    else:
                        max_area = max(max_area, index * heights[previous_index])
            else:  # 如果为空，则入栈
                stack_index.append(index)
                index = index + 1
        return max_area


def test_solution():
    s_obj = Solution()
    assert s_obj.largestRectangleArea([1, 3, 4, 2]) == 6
    assert s_obj.largestRectangleArea([1, 3, 1]) == 3
    assert s_obj.largestRectangleArea([1, 3, 1, 1]) == 4
    assert s_obj.largestRectangleArea([3, 2, 1]) == 4
    assert s_obj.largestRectangleArea([2, 0, 2]) == 2


def test_solution2():
    s_obj = Solution2()
    assert s_obj.largestRectangleArea([1, 3, 4, 2]) == 6
    assert s_obj.largestRectangleArea([1, 3, 1]) == 3
    assert s_obj.largestRectangleArea([1, 3, 1, 1]) == 4
    assert s_obj.largestRectangleArea([3, 2, 1]) == 4
    assert s_obj.largestRectangleArea([2, 0, 2]) == 2
    assert s_obj.largestRectangleArea([0, 3, 2, 5]) == 6


if __name__ == '__main__':
    s_obj = Solution2()
    # s_obj._increase_list([1, 3, 4, 7])
    # s_obj._descrea_list([4, 3, 2, 1])
    res = s_obj.largestRectangleArea([0, 3, 2, 5])
    print(res)
