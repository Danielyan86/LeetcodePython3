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
                    if Grid[line_index - 1][col_index] == -1 and Grid[line_index][col_index - 1] == -1:
                        continue
                    elif Grid[line_index - 1][col_index] == -1 or Grid[line_index][col_index - 1] == -1:
                        Grid[line_index][col_index] = max(Grid[line_index - 1][col_index],
                                                          Grid[line_index][col_index - 1])
                    else:
                        Grid[line_index][col_index] = Grid[line_index - 1][col_index] + \
                                                      Grid[line_index][col_index - 1]
        return Grid[lines - 1][cols - 1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        res = [0] * len(obstacleGrid[0])  # m x n matrix
        res[0] = 1
        for i in obstacleGrid:
            for j, each in enumerate(i):
                if each == 0:
                    if j != 0:
                        res[j] += res[j - 1]
                else:
                    res[j] = 0
        return res[-1]


if __name__ == '__main__':
    test_data = [[1, 0]]
    s_obj = Solution2()
    res = s_obj.uniquePathsWithObstacles(test_data)
    print(res)
