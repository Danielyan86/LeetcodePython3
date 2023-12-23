# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        l, r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            # 如果前面一个也为true，则继续往前找，否则直接返回
            if isBadVersion(mid) and isBadVersion(mid - 1):
                r = mid - 1
            elif isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            else:
                l = mid + 1
        return l
