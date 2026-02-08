class Solution:
    # 二分法
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


# 使用快慢指针大法，更简单，更好理解
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, f = -1, 0
        while f < len(nums):
            if target <= nums[f]:
                return s + 1
            f += 1
            s += 1
        return s + 1


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.searchInsert([1, 3, 5, 6], 2)
    print(res)
