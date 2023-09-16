from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(0, length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # has the same time complex with the first one
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for index, value1 in enumerate(nums):
            for index2, value2 in enumerate(nums[index + 1:]):
                if value1 + value2 == target:
                    return [index, index + index2 + 1]
        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        for index, value1 in enumerate(nums):
            index2 = -1
            value2 = target - value1
            try:
                # find the target index by buildin method index
                index2 = nums[index + 1:].index(value2)
                if index2 != -1:
                    return [index, index + index2 + 1]
                else:
                    continue
            except Exception as e:
                print(index2)
        return []


if __name__ == '__main__':
    sum_obj = Solution()
    print(sum_obj.twoSum([2, 11, 8, 12, 13], target=10))
    print(sum_obj.twoSum2([0, 11, 8, 2, 13], target=10))
    print(sum_obj.twoSum3([3, 2, 4], target=6))
# 这道题能直接想到的就是冒泡排序的算法，但是冒泡算法的时间复杂度高O（n*n）
