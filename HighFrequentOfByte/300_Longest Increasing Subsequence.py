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


## 维护一个升序列表，使用二分发插入
## 如果小于第一个值，则直接替换，不满足升序
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increase = []
        for x in nums:
            i = bisect_left(increase, x)
            if i == len(increase):  # x 位置在最后一个，满足升序，直接append
                increase.append(x)
            else:
                # 这一步最关键，不满足则直接替换对应位置数字
                # 这个地方分两种情况，如果increase为空，相当于直接append，如果已经有数字，则替换对应位置数字
                # 比如【2，5】，来了一个3，这个时候变成2，3，其实长度并没有变
                increase[i] = x
        return len(increase)


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLIS(nums=[1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(res)
