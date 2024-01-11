# 题目： 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 求和，然后判断和是否小于0，因为只要前面的和小于0，那么后面的数加上前面的和就一定比自身小，所以又重新求和，
# 并和之前的最大子序和比较，取最大值。
# 思维盲点：负数越加越少, 搞清楚另起炉灶的判定条件，不是当前数字，而是dp[i-1]是否小于0

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [nums[0]]
        for i in range(1, len(nums)):
            if dp[i - 1] >= 0:
                dp.append(dp[i - 1] + nums[i])
            else:
                dp.append(nums[i])
        return max(dp)


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.maxSubArray([5, 4, -1, 7, 8])
    print(res)
