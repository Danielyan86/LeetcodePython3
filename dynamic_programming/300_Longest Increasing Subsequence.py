from typing import List


# 这题的难点在于怎么根据dp[i]推算出dp[i+1],dp[i+1]没法通过某一个子序列直接推到，需要对比所有的子序列，因此用到max
# 如果更大，表示大于前面上升数列的最后一个值，在前面对应的dp上+1，最后取最大值
# 两次循环，依次和前面比较，在前面对应的dp上+1
# 最后取最大值
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for n in range(1, len(nums)):
            for pre_n in range(n):
                if nums[n] > nums[pre_n]:
                    # 通过max 动态更新pd
                    dp[n] = max(dp[n], dp[pre_n] + 1)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(res)
