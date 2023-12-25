class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def trace(lst):
            # 最后返回条件是空，就是什么都不会append
            if len(lst) == len(nums):
                res.append(lst)
            for i in range(len(nums)):
                if nums[i] not in lst:
                    trace(lst + [nums[i]])

        trace([])
        return res
