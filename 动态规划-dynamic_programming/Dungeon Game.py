# 题目 https://leetcode-cn.com/problems/dungeon-game/description/

# 分析 刚开始时候还是想的是从左上到右下的顺序思维，然后不断更新初始值，
# 这题可以采用逆向思维，即从出口反推回去
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
        for i in reversed(range(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)  # 更新最后一个数字
            for j in reversed(range(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j + 1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)

        return DP[0]


if __name__ == '__main__':
    s_obj = Solution()
    res = s_obj.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    print(res)
