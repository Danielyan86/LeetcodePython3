import pytest
from typing import List

import random


class Solution:
    def partition(self, nums, left, right):
        pivot = nums[left]  # 取左边第一个为哨兵，哨兵最后归位
        l, r = left, right
        while l < r:
            while l < r and nums[r] >= pivot:  # 从右往左，直到找到一个比pivot更小的数
                r -= 1  # 本来就在哨兵右边，不用做任何操作，直接移动指针
            nums[l] = nums[r]  # 将更小的数放入左边，左边数字已经存在pivot了，不怕覆盖
            while l < r and nums[l] <= pivot:  # 从左往右找，直到找到一个比pivot更大的数
                l += 1
            nums[r] = nums[l]  # 将更大的数放入右边
        # 循环结束，l与r相等
        nums[l] = pivot  # 待比较数据放入最终位置
        return l  # 返回待比较数据最终位置)

    # 分区采用的原地交换法，不再通过递归返回排列好的数组
    def quicksort(self, nums, left, right):
        if left < right:  # 如果l==r,表示长度相等，直接返回
            index = self.partition(nums, left, right)  # index位置不会再变，重新划分分区递归调用
            self.quicksort(nums, left, index - 1)
            self.quicksort(nums, index + 1, right)
        return nums


@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        (
            [
                3,
                1,
                4,
                1,
                5,
                9,
                2,
                6,
                5,
                3,
            ],
            [1, 1, 2, 3, 3, 4, 5, 5, 6, 9],
        ),
    ],
)
def test_quick_sort(input_list, expected_output):
    s = Solution()
    result = s.quicksort(input_list, 0, len(input_list) - 1)
    assert result == expected_output


if __name__ == "__main__":
    test_quick_sort()
