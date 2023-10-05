# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。


# 思路：遍历每一个柱子，也就是数组中每一个元素，以这个元素为中心，找到最大的面积,当前元素的值即为长方形的高
# 时间复杂度应为n*n
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        Rectangle_area = 0
        for index, height in enumerate(heights):
            width = 1
            heights_len = len(heights)
            left_index, right_index = index, index
            if height > 0:
                while left_index > 0:
                    if heights[left_index - 1] >= height:
                        width += 1
                        left_index = left_index - 1
                    else:
                        break
                while right_index < heights_len - 1:
                    if heights[right_index + 1] >= height:
                        width += 1
                        right_index = right_index + 1
                    else:
                        break
                Rectangle_area = max(Rectangle_area, width * height)
        return Rectangle_area


class Solution2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        pass


def test_solution():
    s_obj = Solution()
    assert 10 == s_obj.largestRectangleArea([2, 1, 5, 6, 2, 3])


if __name__ == "__main__":
    s_obj = Solution()
    test_data = [0]
    res = s_obj.largestRectangleArea(test_data)
