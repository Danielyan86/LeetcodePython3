# 注意是返回下标，而不是target数字
# 整个思路是不断缩小有序空间的范围，让目标数字必然出现在一个有序区间里面
# 如果不存在，则直接返回-1
# 始终根据有序区间移动指针始终只关心有序的那个区间即可
# 另外一边反着写即可


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
            if nums[l] <= nums[mid]:  # 只用判断满足此条件左边有序，否则右边必然有序
                if nums[l] <= target < nums[mid]:  # 如果目标数字在这个有序空间，则移动右指针
                    r = mid - 1
                else:
                    l = mid + 1  # 如果不在，则移动左指针
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return mid
