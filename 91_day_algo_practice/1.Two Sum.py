class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_d = dict()
        for i, num in enumerate(nums):
            if target - num in index_d:
                return [index_d[target - num], i]
            index_d[num] = i
