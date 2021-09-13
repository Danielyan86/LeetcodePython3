from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.qsort(nums, k)

    def qsort(self, nums: List[int], k: int):
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums[0]
            left_list = [x for x in nums[1:] if x >= pivot]
            right_list = [x for x in nums[1:] if x <= pivot]
            new_list = left_list + [pivot] + right_list
            pivot_index = new_list.index(pivot) + 1
            if pivot_index == k:
                return pivot
            elif pivot_index > k:
                return self.qsort(left_list, k)
            elif pivot_index < k:
                return self.qsort(right_list, k - pivot_index)


if __name__ == '__main__':
    s = Solution()
    res = s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(res)
