# 题目
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？


# 破题思路：在之前简单迷宫的基础上加了障碍物，通过图形推导发现只需要在上一个A[x][Y]=A[x-1][Y]+A[x][Y-1]的基础上加一个判断，
# 因为有障碍，所以迷宫不像上一个简单迷宫是自己生成，只能更新输入迷宫里面初始化值
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type Grid: List[List[int]]
        :rtype: int
        """
        Grid = obstacleGrid
        lines, cols = len(Grid), len(Grid[0])
        if Grid[lines - 1][cols - 1] == 1 or Grid[0][0] == 1:  # 如果终点或者起点为障碍，则永远无法到达
            return 0
        # 因为数字1需要用来计算路径，所以先把表示障碍的1更新为-1, 并初始化边界值
        if lines == 1 and cols == 1:
            return 1 if Grid[lines - 1][cols - 1] == 0 else 0
        for line, line_list in enumerate(Grid):
            for col, num in enumerate(line_list):
                if num == 1:
                    Grid[line][col] = -1
        Grid[0][0] = 1

        # 初始化第一行边界值，如果遇到-1，则-1后面无法到达，因此停止复制，保持为0
        for index, num in enumerate(Grid[0]):
            if num != -1:
                Grid[0][index] = 1
            else:
                break
        # 初始化第一列边界值，如果遇到-1，则-1后面无法到达，因此为0
        for line, line_list in enumerate(Grid):
            if line_list[0] != -1:
                Grid[line][0] = 1
            else:
                break

        for line_index in range(1, lines):
            for col_index in range(1, cols):
                if Grid[line_index][col_index] != -1:
                    if (
                        Grid[line_index - 1][col_index] == -1
                        and Grid[line_index][col_index - 1] == -1
                    ):
                        continue
                    elif (
                        Grid[line_index - 1][col_index] == -1
                        or Grid[line_index][col_index - 1] == -1
                    ):
                        Grid[line_index][col_index] = max(
                            Grid[line_index - 1][col_index],
                            Grid[line_index][col_index - 1],
                        )
                    else:
                        Grid[line_index][col_index] = (
                            Grid[line_index - 1][col_index]
                            + Grid[line_index][col_index - 1]
                        )
        return Grid[lines - 1][cols - 1]


class Solution2:
    # 更简单的一种解决方案，因为是直接遍历，时间复杂度还要跟低一些，核心算法时间复杂度是一样的，是O(m*n)，空间上会多出一个为n长度的一维列表
    # 其实本质上还是A[x][Y]=A[x-1][Y]+A[x][Y-1]，但是巧妙的利用了一个一维列表来维持每行的步数，这样每次数据存的是当前行每一个格子所需步数
    # 遍历完成之后，res列表最优一个存储就是结果
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res = [0] * len(obstacleGrid[0])  # 初始化一个长度为列长度的一维数组，
        res[0] = 1
        for line_idx in obstacleGrid:
            for col_idx, each in enumerate(line_idx):
                if each == 0:  # 如果值为0，不是障碍
                    if col_idx != 0:  # 并且索引不为0，不是第一列
                        # 则等于列表当前值加上前一项的值，相当于这个列表再一直循环累加
                        res[col_idx] += res[col_idx - 1]
                else:
                    res[col_idx] = 0  # 是障碍时候则设置值为0
        return res[-1]  # 返回最后一个


if __name__ == "__main__":
    test_data = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    s_obj = Solution2()
    res = s_obj.uniquePathsWithObstacles(test_data)
    print(res)
