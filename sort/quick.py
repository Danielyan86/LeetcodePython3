import pytest
from typing import List


class Solution:
    def quick(self, nums: List[int]) -> List[int]:
        # 注意递归返回条件
        if len(nums) <= 1:
            return nums
        if len(nums) == 0:
            return []
        pivot = nums[0]
        # 分区比较
        return (
            self.quick([x for x in nums[1:] if x <= pivot])
            + [pivot]
            + self.quick([x for x in nums[1:] if x > pivot])
        )


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
    result = s.quick(input_list)
    assert result == expected_output


if __name__ == "__main__":
    test_quick_sort()
