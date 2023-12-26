class Solution:
    # 因为都是正整数，实际最多出现跳过两个数字情况，不会跳过更多了
    # 如果有两个大数字，要么相邻，要么隔一个小的，或者两个，只有这3种情况
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        a, b = nums[0], max(nums[0], nums[1])  # 注意第二个b表示取大，而不是直接取第二个
        for i in range(2, n):
            a, b = b, max(nums[i] + a, b)
        return b
