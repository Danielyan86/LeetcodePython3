class Solution:
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


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.searchInsert([1, 3, 5, 6], 2)
    print(res)
