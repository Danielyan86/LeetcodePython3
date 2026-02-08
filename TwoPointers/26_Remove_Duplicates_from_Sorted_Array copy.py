from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        s, f = 0, 1  # 快慢指针初始化
        while f < len(nums):
            if nums[s] != nums[f]:  # 这里很tricky，为什么是移动慢指针的下一个，因为快指针有越界风险
                nums[s + 1] = nums[f]  # 核心代码其实就这一句，用后面不重复数字覆盖前面重复个数字
                s += 1
            f += 1  # 无论什么情况快指针都需要移动一格
        return s + 1

    # 错误例子，留在这看以前code是多么stupid！
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
