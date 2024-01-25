class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 将数组中所有元素进行异或操作，得到两个只出现一次的数字的异或结果
        import functools

        xor_all = functools.reduce(xor, nums)
        # 找到异或结果中的最低位的1（低位第一个不同的位）
        lowbit = xor_all & -xor_all
        # 初始化结果数组
        ans = [0, 0]
        # 根据最低位的1，将数组分为两组，每组包含一个只出现一次的数字
        for x in nums:
            ans[(x & lowbit) != 0] ^= x  # 分组异或
        return ans
