from typing import List


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]  # 巧用del关键字，比remove，pop可读性更高
            else:
                i += 1
        print(nums)
        return i

    # new version
    def removeDuplicates2(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
                continue
            elif nums[i] < nums[j]:
                i = i + 1
                j = i + 1
        return len(nums)

    # 快慢指针实现，相比起第二个实现方案，不会改变原有数组长度，只是把原有的重复数据重新排序
    # 把重复的数据通过交换方式放到后面去，这样慢指针永远是指到的不重复的一个数字
    # 判断的细节要多一些，更容易出错
    def removeDuplicates3(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        slow_p = 0
        fast_p = slow_p + 1
        while fast_p < len(nums):
            if nums[slow_p] == nums[fast_p]:
                fast_p = fast_p + 1
            elif nums[slow_p] < nums[fast_p]:
                if fast_p - slow_p == 1:
                    slow_p = slow_p + 1
                    fast_p = fast_p + 1
                elif fast_p - slow_p > 1:
                    slow_p = slow_p + 1
                    nums[slow_p], nums[fast_p] = nums[fast_p], nums[slow_p]
                    fast_p = fast_p + 1
        print(nums)
        return slow_p + 1


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.removeDuplicates([1, 4, 4, 4, 5, 6, 6, 7])
    print(res)

    res = s_obj.removeDuplicates2([1, 2, 3])
    print(res)
    res = s_obj.removeDuplicates3([1, 4, 4, 4, 5, 6, 6, 7])
    print(res)
