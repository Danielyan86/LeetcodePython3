class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        if len(right) >= k:  # 注意边界值要取等号
            return self.findKthLargest(right, k)
        if len(left) > len(nums) - k:
            # 想想线段图，k到小区间右边值应该是   左边区域长度-（总长度-k）
            return self.findKthLargest(left, len(left) - (len(nums) - k))  # 注意k的位置需要重新计算
        return pivot
