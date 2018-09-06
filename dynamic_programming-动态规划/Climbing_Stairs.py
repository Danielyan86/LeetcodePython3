# 题目：假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 思路：通过分析发现是一个斐波那契数列，既每一项等于前两项之和，通过动态规划求解，推导式

# 递归方法
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            one_step = self.climbStairs(n - 1)
            two_step = self.climbStairs(n - 2)
        return one_step + two_step


# 动态规划
class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 2
        if n == 1:
            return a
        elif n == 2:
            return b
        elif n > 2:
            for i in range(n - 1):
                a, b = b, a + b
            return a


if __name__ == '__main__':
    test_data = 35
    # s_obj = Solution()
    # res = s_obj.climbStairs(test_data)
    # print(res)
    s_obj = Solution2()
    res = s_obj.climbStairs(test_data)
    print(res)
