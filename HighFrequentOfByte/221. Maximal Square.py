class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # Create a 2D DP array to store the maximum side length of squares
        dp = [[0] * n for _ in range(m)]

        max_side = 0  # Variable to track the maximum side length

        # Fill the DP array
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    # If the current cell is '1', calculate the maximum side length
                    if i == 0 or j == 0:  # 如果是左上角第一个格子，则直接给1
                        dp[i][j] = 1
                    else:
                        # 前面三个格子取最小值 再+1即可，最小值确定了可以和当前格子组成的最小正方形
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    # Update the maximum side length
                    max_side = max(max_side, dp[i][j])  # 因为是2d的，需要每次更新最大边长

        return max_side * max_side  # Return the area of the largest square
