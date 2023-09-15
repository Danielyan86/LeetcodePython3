from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0:
            return []

        lp, rp = 0, len(nums) - 1
        while lp<rp:

