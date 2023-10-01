# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        count_list = triangle[-1]
        triangle = triangle[:-1]
        for num_line in reversed(triangle):
            for index, value in enumerate(num_line):
                count_list[index] = value + \
                    min(count_list[index], count_list[index + 1])
        return count_list[0]


def test_minimumTotal():
    s_obj = Solution()
    assert 11 == s_obj.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    assert -1 == s_obj.minimumTotal([[-1], [2, 3], [1, -1, -3]])


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
    print(res)
