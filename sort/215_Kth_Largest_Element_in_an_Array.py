class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            small, big = [x for x in nums if x < pivot], [x for x in nums if x > pivot]
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            # 三个区间长度比较看k落在哪个区间，要么大，要么小，要么刚好中间
            if len(big) >= k:
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(small) > len(nums) - k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - len(nums) + len(small))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)
