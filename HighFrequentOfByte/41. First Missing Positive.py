# 不用什么排序，二分法，搞复杂了
#  先转化成set去重
# 假设缺失最小的正整数为1，开始每次加一，如果存在就一直+1，直到找到一个不存在的数字
# 和寻找一个连续范围缺失数字类似
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)  # Remove duplicates using a set
        smallest_positive = 1

        while smallest_positive in nums:
            smallest_positive += 1

        return smallest_positive
