import pytest
from typing import List


class Solution:
    def insert_sort(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]  #  依次往后移动也就是所谓的搬运 用当前值覆盖后一个值
                j -= 1
            nums[j + 1] = key  # 没有进入循环，自己覆盖自己
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
def test_insert_sort(input_list, expected_output):
    s = Solution()
    result = s.insert_sort(input_list)
    assert result == expected_output


if __name__ == "__main__":
    test_insert_sort()
