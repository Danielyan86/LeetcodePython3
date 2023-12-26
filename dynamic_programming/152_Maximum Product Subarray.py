class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            # Swap max and min products if the current number is negative
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            # Update the max and min products ending at the current position
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            # Update the overall result
            result = max(result, max_product)

        return result
