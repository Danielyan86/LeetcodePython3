class Solution:
    # 动态规划，和https://leetcode.cn/problems/min-cost-climbing-stairs/description/
    # 基本类似，只不过爬楼梯是找最小开销，这个是找最大费用
    # 从最小集合开始推导，如果是3个格子，第三个要取最大，要么1+3格子值最大，要么取第二个
    # 通过推到发现当前最大值只和前面两个格子有关，可以优化内存空间
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a, b = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            a, b = b, max(nums[i] + a, b)
        return b
