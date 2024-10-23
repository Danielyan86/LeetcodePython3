from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        O(n^2) algo:
        """
        nums.sort()
        res = set()
        if nums[0] > 0:
            return []
        for i, v in enumerate(nums):
            if i < len(nums) - 2:
                l, r = i + 1, len(nums) - 1
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                while l < r:
                    sum3 = v + nums[l] + nums[r]
                    if sum3 == 0:
                        res.add((v, nums[l], nums[r]))
                        l, r = l + 1, r - 1
                    elif sum3 < 0:
                        l += 1
                    elif sum3 > 0:
                        r -= 1

        return list(res)


# 双指针使用的前置条件是有序数组
# 双指针的思路理清楚之后，此题思路并不困难，但是细节的把握是难点，怎么保证循环正确的跳出和边界值的设定
if "__main__" == __name__:
    S = Solution()
    res = S.threeSum([-1, -2, 0, 0, 0, 1, 2, 3])
    print(res)
