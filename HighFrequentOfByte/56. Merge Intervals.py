from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照list第一个元素大小进行排序
        intervals.sort(key=lambda x: x[0])

        res = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            # 比较是和上一个空间右边边界大小
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                # 也就是把右边界更新成更大的那一个
                res[-1][1] = max(res[-1][1], interval[1])

        return res


if __name__ == "__main__":
    s = Solution()
    res = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(res)
