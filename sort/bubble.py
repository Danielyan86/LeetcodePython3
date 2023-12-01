import pytest
from typing import List


class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j + 1] < nums[j]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
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
def test_bubble_sort(input_list, expected_output):
    s = Solution()
    result = s.bubble_sort(input_list)
    assert result == expected_output


if __name__ == "__main__":
    test_bubble_sort()
