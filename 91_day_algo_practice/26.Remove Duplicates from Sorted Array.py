class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                nums[l + 1] = nums[r]
                l += 1
        return l + 1
