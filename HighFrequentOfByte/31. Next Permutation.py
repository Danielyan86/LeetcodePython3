class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        l, r, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        # 先通过双指针大法找到变化的那个点
        # 假设从右往左一直上坡，找到第一个下降段后进入第二个循环
        while l >= 0 and nums[l] >= nums[r]:
            l, r = l - 1, r - 1
            # 找到需要交换的那个数字 ，山坡右边的点高于左边
        # 有可能一直上坡，则不存在，也就是是一个下降序列，跳过交换这一步，直接整个序列全部翻转
        if l >= 0:
            while nums[l] >= nums[k]:
                k -= 1
            nums[l], nums[k] = nums[k], nums[l]
        # 剩下的数字反转
        nums[r:] = nums[r:][::-1]


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        l, r, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while l >= 0:
            if nums[l] >= nums[r]:
                l -= 1
                r -= 1
            else:
                break  # 不要忘了break
        # 如果遍历完了都一直是上升的，那么l，r的值分别为-1，0，
        # 只有找到了才交换，否则剩下的直接反转
        if l >= 0:
            while k > 0:
                if nums[k] > nums[l]:
                    nums[l], nums[k] = nums[k], nums[l]
                    break  # 不要忘了break
                k -= 1
        nums[r:] = nums[r:][::-1]
