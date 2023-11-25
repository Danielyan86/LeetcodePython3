from typing import List


# 这题的难点在于怎么根据dp[i]推算出dp[i+1],dp[i+1]没法通过某一个子序列直接推到，需要对比所有的子序列，因此用到max
# 如果更大，表示大于前面上升数列的最后一个值，在前面对应的dp上+1，最后取最大值
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n - 1):
            for sub_i in range(i + 1):
                if nums[i + 1] > nums[sub_i]:
                    dp[i + 1] = max(dp[i + 1], dp[sub_i] + 1)

        return max(dp)


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(res)
