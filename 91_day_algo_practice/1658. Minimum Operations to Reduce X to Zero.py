class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:  # 小于0，则不存在
            return -1
        res = -1
        l = 0
        sum_n = 0
        for r, v in enumerate(nums):
            sum_n += v
            while sum_n > target:
                sum_n -= nums[l]
                l += 1
            if sum_n == target:
                res = max(res, r - l + 1)
        return -1 if res < 0 else len(nums) - res
