from typing import List


class Solution:
    # use dimensionality thoughts to convert 3 sum problem into 2 sum problem
    # the array must be sorted if using 2 pointers to solve it.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        if nums[0] > 0:
            return []
        res = []
        for base_i in range(0, len(nums) - 2):
            base_v = nums[base_i]
            if base_v > 0:  # 至少有一个数字小于0，不可能三个数字大于0
                break
            point_l, point_r = base_i + 1, len(nums) - 1
            while point_l < point_r:
                if nums[point_l] + nums[point_r] == -base_v:
                    sum_zero = [base_v, nums[point_l], nums[point_r]]
                    # remove the duplicate one
                    if sum_zero not in res:
                        res.append(sum_zero)
                    point_l = point_l + 1
                elif nums[point_l] + nums[point_r] > -base_v:
                    point_r = point_r - 1
                elif nums[point_l] + nums[point_l] < -base_v:
                    point_l = point_l + 1
        return res


# 双指针使用的前置条件是有序数组
# 双指针的思路理清楚之后，此题思路并不困难，但是细节的把握是难点，怎么保证循环正确的跳出和边界值的设定
if "__main__" == __name__:
    S = Solution()
    res = S.threeSum([-1, -2, 0, 0, 0, 1, 2, 3])
    print(res)
