from typing import List
import collections


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 字典存的是索引，不是个数，不用关心字典顺序，始终可以通过l找到左边key
        ld = {}  # Dictionary to store the last index of each fruit
        l = 0  # l index of the current subarray
        max_l = 0  # Length of the longest subarray

        for r, fruit in enumerate(fruits):
            ld[fruit] = r  # Update the last index of the current fruit

            # If the number of distinct fruits exceeds 2, adjust the l index
            while len(ld) > 2:
                if ld[fruits[l]] == l:
                    del ld[fruits[l]]
                l += 1

            max_l = max(max_l, r - l + 1)  # Update the longest subarray length

        return max_l


if __name__ == "__main__":
    s = Solution()
    res = s.totalFruit([1, 2, 2, 1, 3, 3, 3, 3, 3, 3])
