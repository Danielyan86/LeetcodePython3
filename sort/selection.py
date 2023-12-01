import pytest
from typing import List


class Solution:
    def selection(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
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
def test_selection_sort(input_list, expected_output):
    s = Solution()
    result = s.selection(input_list)
    assert result == expected_output


if __name__ == "__main__":
    test_selection_sort()
