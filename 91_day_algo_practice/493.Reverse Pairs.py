from typing import List
import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n2_lst, res = [], 0
        for n in nums[::-1]:
            res += bisect.bisect_left(n2_lst, n)
            n2 = 2 * n
            idx = bisect.bisect_left(n2_lst, n2)
            n2_lst.insert(idx, n2)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.reversePairs([1, 3, 2, 3, 1])
    print(res)
