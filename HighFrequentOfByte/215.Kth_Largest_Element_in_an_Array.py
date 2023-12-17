class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, k):
            pivot = random.choice(nums)
            samll, big = [x for x in nums if x < pivot], [x for x in nums if x > pivot]
            mid = [x for x in nums if x == pivot]
            if len(big) >= k:  # 注意边界值要取等号
                return quick_sort(big, k)
            if len(samll) > len(nums) - k:
                return quick_sort(samll, k - (len(nums) - len(samll)))  # 注意k的位置需要重新计算
            return pivot

        return quick_sort(nums, k)
