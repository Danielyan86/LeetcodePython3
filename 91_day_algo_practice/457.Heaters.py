class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = 0
        heaters.sort()  # 加热器排序
        for h in houses:  # 把房屋依次插入heaters list计算距离
            r = bisect.bisect_right(heaters, h)  # 找到最右边插入位置
            l = r - 1
            rightDistance = heaters[r] - h if r < len(heaters) else float("inf")  # 注意边界的处理
            leftDistance = h - heaters[l] if l >= 0 else float("inf")
            curDistance = min(leftDistance, rightDistance)
            res = max(res, curDistance)
        return res
