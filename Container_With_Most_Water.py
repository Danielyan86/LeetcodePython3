class Solution:
    def maxArea_violent(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height = [0] + height
        length = len(height)
        max_water_container = 0
        if length >= 2:
            for i in range(0, length - 1):
                for j in range(i + 1, length):
                    hight_min = min(height[i], height[j])
                    max_water_container = max(
                        max_water_container, hight_min * (j - i))
            return max_water_container
        else:
            return 0

    def maxArea(self, height):
        max_area = 0
        height = [0] + height
        length = len(height)
        left_pointer, right_pointer = 1, length - 1
        if length >= 2:
            while left_pointer < right_pointer:
                max_area = max(min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer),
                               max_area)
                if height[left_pointer] < height[right_pointer]:
                    left_pointer = left_pointer + 1
                else:
                    right_pointer = right_pointer - 1
        return max_area

    # 此题关键破题点是双指针怎么移动问题
    # 无论左移还是右移，宽度都是减小，因此只能移动高度更短的一边，面积才可能增加,因为面积是由高度最低的木板决定的
    def maxArea2(self, height: List[int]) -> int:
        # 但凡用min，max这一类函数，都需要一个初始值,最小或者无限大
        if len(height) < 2:
            return None
        maxArea = 0
        point_l, point_r = 0, len(height) - 1
        while point_l < point_r:
            temp_area = min(height[point_l],
                            height[point_r]) * (point_r - point_l)
            maxArea = max(temp_area, maxArea)
            if height[point_l] <= height[point_r]:
                point_l = point_l + 1
            else:
                point_r = point_r - 1
        return maxArea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    s_obj = Solution()
    res = s_obj.maxArea(height)
    print(res)
