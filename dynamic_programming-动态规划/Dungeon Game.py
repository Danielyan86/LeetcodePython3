# 题目 https://leetcode-cn.com/problems/dungeon-game/description/

# 分析 刚开始时候还是想的是从左上到右下的顺序思维，然后不断更新初始值，
# 这题应该采用逆向思维，即从出口反推回去，因为限定条件是出来时候为1，所以初始值是确定的，如果从入口开始，则初始值是不确定的，
# 有点像解方程，因为计算机不会自动解方程，需要用逆向思维反推回去
# 要注意再任意时刻血量不能低于0，即和为正数，要起始值最低，即每一步选择和为最大值

class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        # 初始化一位数组，长度为列数目，每个值为无限大
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1  # 退出时候值为1，

        # 从最后一个格子开始，反向遍历二维数组
        for row_idx in reversed(range(len(dungeon))):
            # 顺序过来每到一个格子是+，反着回去就是-，如果最后一个格子为正数，则取最后一个格子的值，如果为0或者负数，则取1，因为每个时候状态需要大于1
            DP[-1] = max(DP[-1] - dungeon[row_idx][-1], 1)
            for col_idx in reversed(range(len(dungeon[row_idx]) - 1)):  # 最后一列倒数第二个格子开始，初始化最后一列
                min_HP_on_exit = min(DP[col_idx], DP[col_idx + 1])  # 更新退出血量
                # 如果是一个负数，则加上一个血量，因为。如果是正数，则减去。如果减去一个正数小于1了，证明这个格子加血量已经够了，则更新为1
                DP[col_idx] = max(min_HP_on_exit - dungeon[row_idx][col_idx], 1)

        return DP[0]


class Solution2:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        rows, cols = len(dungeon), len(dungeon[0]),
        if cols == 1:
            return 1 if dungeon[0][0] > 0 else abs(dungeon[0][0]) + 1
        else:
            # min_HP_on_exit = 1
            dungeon[rows - 1][cols - 1] = 1 if 1 - dungeon[rows - 1][cols - 1] < 0 else 1 - dungeon[rows - 1][cols - 1]
            # 遍历二维数组，根据规则，到达每一个格子应该为正数
            for row in reversed(range(rows)):
                for col in reversed(range(cols)):
                    if row == rows - 1 and col == cols - 1:
                        continue
                    elif row == rows - 1:  # 初始化最后一行
                        dungeon[row][col] = max(dungeon[row][col + 1] - dungeon[row][col], 1)
                    elif col == cols - 1:  # 初始化最后一列
                        dungeon[row][col] = max(dungeon[row + 1][col] - dungeon[row][col], 1)
                    else:
                        dungeon[row][col] = max(min(dungeon[row + 1][col] - dungeon[row][col],
                                                    dungeon[row][col + 1] - dungeon[row][col]), 1)
            return dungeon[0][0]


def test_solition2():
    test_data = [[0]]
    s_obj = Solution2()
    res = s_obj.calculateMinimumHP(test_data)
    assert res == 1


if __name__ == '__main__':
    test_data = [[0]]
    s_obj = Solution()
    res = s_obj.calculateMinimumHP(test_data)
    print(res)
    s_obj = Solution2()
    res = s_obj.calculateMinimumHP(test_data)
    print(res)
