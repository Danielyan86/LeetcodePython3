from typing import List


class Solution:
    # use dimensionality thoughts to convert 3 sum problem into 2 sum problem
    # the array must be sorted if using 2 pointers to solve it.

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0:
            return []
        res = []
        for i in range(len(nums) - 3):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return res


# 双指针使用的前置条件是有序数组
# 双指针的思路理清楚之后，此题思路并不困难，但是细节的把握是难点，怎么保证循环正确的跳出和边界值的设定
if "__main__" == __name__:
    S = Solution()
    res = S.threeSum([-1, -2, 0, 0, 0, 1, 2, 3])
    print(res)
