class Solution:
    class Solution:
        def numWays(self, n: int) -> int:
            if n == 0 or n == 1:
                return 1
            if n == 2:
                return 2
            a, b = 1, 2
            for num in range(3, n + 1):
                a, b = b, a + b
            return b % 1000000007


if __name__ == "__main__":
    s = Solution()
    res = s.numWays(4)
    print(res)
