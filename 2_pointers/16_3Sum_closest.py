from typing import List


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        difference_num = float("inf")
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                left_point = i + 1  # 指针每次不用从第一个开始，因为加法交换律
                right_point = len(nums) - 1
                while left_point < right_point:
                    three_sum = nums[i] + nums[left_point] + nums[right_point]
                    res = three_sum - target
                    if res == 0:
                        return three_sum
                    elif res < 0:
                        if abs(res) < difference_num:  # 判定更新结果条件
                            result = three_sum
                        left_point += 1
                    elif res > 0:
                        if abs(res) < difference_num:
                            result = three_sum
                        right_point -= 1
                    difference_num = min(abs(res), difference_num)
        return result

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        # assume the difference value is infinite
        if len(nums) == 0:
            return None
        elif len(nums) < 3:
            return sum(nums)
        nums.sort()
        diff_abs = float("inf")
        for base_i in range(len(nums)):
            point_l = base_i + 1
            point_r = len(nums) - 1
            while point_l < point_r:
                three_sum = nums[base_i] + nums[point_l] + nums[point_r]
                diff = three_sum - target
                if diff > 0:
                    point_r = point_r - 1
                    if abs(diff) < diff_abs:
                        res = three_sum
                elif diff < 0:
                    point_l = point_l + 1
                    if abs(diff) < diff_abs:
                        res = three_sum
                elif diff == 0:
                    return three_sum
            # don't forget to update the diff_abs
                diff_abs = min(abs(diff), diff_abs)
        return res

        # 题目转化一下其实还是三数之和的变体，也就是三数之和和目标数字的绝对值最小, problem converting must be understand


# 无穷大怎么设定，绝对值内置函数的调用
if __name__ == '__main__':
    nums = [0, 2, 1, -3]
    s_obj = Solution()
    print(s_obj.threeSumClosest(nums, 1))
    print(s_obj.threeSumClosest(nums, 1))
