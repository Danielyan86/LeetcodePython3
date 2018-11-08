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


class Solution2:
    def largestRectangleArea(self, heights: list) -> int:
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(-1)
        index, max_area = 0, 0
        index_stack = []
        while index < len(heights):
            # 若高度为升序,或者索引栈为空，索引值则入栈，不计算面积
            if len(index_stack) == 0 or heights[index_stack[-1]] <= heights[index]:
                index_stack.append(index)
                index = index + 1
            else:
                # 若开始降序，求局部升序柱子的最大面积
                top = index_stack.pop()  # 若高度开始降序，则把最后一个出栈，也就是上一个最高的柱子序号，每次弹出一个最高柱子，直到为空
                if len(index_stack) == 0:  # 如果栈为空，10有一个柱子，面积为一个柱子的高度，2）降序排列情况，则长方形高度为当前值
                    area = heights[top] * index
                else:  # 如果不为空，先求刚刚弹出的最高柱子的面积，然后求次高柱子和最高柱子的最大面积，以此类推
                    # 因为是升序排列，所以次高柱子就是我们每次求的长方形的高度
                    area = heights[top] * (index - index_stack[-1] - 1)
                max_area = max(max_area, area)
        return max_area


def test_solution():
    s_obj = Solution()
    assert s_obj.largestRectangleArea([1, 3, 4, 2]) == 6
    assert s_obj.largestRectangleArea([1, 3, 1]) == 3
    assert s_obj.largestRectangleArea([1, 3, 1, 1]) == 4
    assert s_obj.largestRectangleArea([3, 2, 1]) == 4


def test_solution2():
    s_obj = Solution2()
    assert s_obj.largestRectangleArea([1, 3, 4, 2]) == 6
    assert s_obj.largestRectangleArea([1, 3, 1]) == 3
    assert s_obj.largestRectangleArea([1, 3, 1, 1]) == 4
    assert s_obj.largestRectangleArea([3, 2, 1]) == 4


if __name__ == '__main__':
    s_obj = Solution2()
    res = s_obj.largestRectangleArea([1, 3, 4, 2])
    print(res)
