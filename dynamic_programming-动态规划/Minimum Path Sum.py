# 题目：给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 说明：每次只能向下或者向右移动一步。

# 思路：到达一个点只有两条路径，算出到达每一个点的最小值即可
# 更新二位数组的值即可


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # res = [0] * len(grid[0])
        # res[0] = grid[0][0]
        if grid:
            if len(grid[0]) == 1:
                return grid[0][0]
            for line_dix, line in enumerate(grid):
                for col_dix, num in enumerate(line):
                    if line_dix == 0 and col_dix == 0:  # 若为起点，则结束
                        continue
                    elif line_dix == 0 and col_dix != 0:  # 第一行赋值
                        grid[line_dix][col_dix] += grid[line_dix][col_dix - 1]
                    elif col_dix == 0 and line_dix != 0:  # 第一列赋值
                        grid[line_dix][col_dix] += grid[line_dix - 1][col_dix]
                    else:  # 求最小值，到达一个点只有两条路径，向下和向右，选择更小的一个值
                        grid[line_dix][col_dix] = (
                            min(grid[line_dix - 1][col_dix], grid[line_dix][col_dix - 1]) + grid[line_dix][col_dix]
                        )
            return grid[line_dix][col_dix]


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(res)
