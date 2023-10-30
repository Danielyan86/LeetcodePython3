class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1和s2都是变化的，dp可以二维数组标记
        # dp[i][j] 可以借助迷宫模型联想,类似迷宫问题从左上角到右下角
        # 特别需要注意的是，dp[i][j]是二维的，s3是一维的，一次实际只能取一个值，初始值dp[0][0]其实表示s1和s2都还没取的时候
        # 这个是最坑的，因此s1，2不能从默认下标0开始，应该是1，开始

        n, m, t = len(s1), len(s2), len(s3)

        if n + m != t:
            return False

        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[p]
                if j > 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[p]
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    res=s.isInterleave(s1, s2, s3)
    print(res)
