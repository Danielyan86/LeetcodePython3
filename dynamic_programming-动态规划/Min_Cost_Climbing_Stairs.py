# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。


# 思路：跟爬楼梯思路基本一致，因为退出的位置是一定的，采倒推法，在数组最后补一个零
# 其实就是算到达每一步的最小值 f[i]=min(f[i-1] , f[i-2]) + f[i]
class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        cost = list(reversed(cost))
        for idx in range(2, len(cost)):
            cost[idx] += min(cost[idx - 1], cost[idx - 2])
        return min(cost[idx], cost[idx - 1])


def test_solution():
    s_obj = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    assert 6 == s_obj.minCostClimbingStairs(cost)
    cost = [10, 15, 20]
    assert 15 == s_obj.minCostClimbingStairs(cost)


if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    s_obj = Solution()
    res = s_obj.minCostClimbingStairs(cost)
    print(res)
