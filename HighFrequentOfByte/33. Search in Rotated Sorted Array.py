# 注意是返回下标，而不是target数字
# 如果不存在，则直接返回-1
# 始终根据有序区间移动指针，只关心其中一个指针就好


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        # if len(nums)==1: return 0
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return mid
