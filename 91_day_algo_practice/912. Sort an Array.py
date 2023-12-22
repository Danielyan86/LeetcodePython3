class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        pivot = random.choice(nums)
        return (
            self.sortArray([x for x in nums if x < pivot])
            + [x for x in nums if x == pivot]
            + self.sortArray([x for x in nums if x > pivot])
        )
