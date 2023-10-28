from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        (
            cur_i,
            cur_max_i,
        ) = (
            0,
            0,
        )
        end_i = len(nums)
        for cur_i, step in enumerate(nums):
            cur_max_i = max(cur_max_i, cur_i + step)
            if cur_max_i >= end_i:
                return True
            if cur_i == cur_max_i and nums[cur_i] == 0:
                return False


if __name__ == "__main__":
    s = Solution()
    res = s.canJump([0])
    print(res)
