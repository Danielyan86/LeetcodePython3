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


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.removeDuplicates([1, 4, 4, 5, 6, 6, 7])
    print(res)

    res = s_obj.removeDuplicates2([1, 2, 3])
    print(res)
