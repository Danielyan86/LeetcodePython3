class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return l + 1


if __name__ == "__main__":
    s = Solution()
    res = s.mySqrt(8)
    print(res)
