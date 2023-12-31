class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        # 双指针大法倒着找
        l, r, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        # find: A[l]<A[r] 倒着找到第一个下降段
        while l >= 0 and nums[l] >= nums[r]:
            l -= 1
            r -= 1

        if l >= 0:  # Not the last permutation
            # find: A[i]<A[k]
            while nums[l] >= nums[k]:
                k -= 1
            # swap A[i], A[k]
            nums[l], nums[k] = nums[k], nums[l]

        # reverse A[j:end]
        r, end = r, len(nums) - 1
        while r < end:
            nums[r], nums[end] = nums[end], nums[r]
            r += 1
            end -= 1
