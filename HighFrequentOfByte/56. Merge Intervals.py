from typing import List

# 利用数组单调自增性质


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 默认·就是按照数组里面从左往右的顺序排序 不用再单独传lambda
        if len(intervals) == 1:
            return intervals
        intervals.sort()

        merged = list()
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 更新右边界即可
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged


if __name__ == "__main__":
    s = Solution()
    res = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(res)
