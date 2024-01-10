## 维护一个升序列表，使用二分发插入
## 如果小于第一个值，则直接替换，不满足升序
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increase = []
        for x in nums:
            i = bisect_left(increase, x)
            # 需要注意边界值是==，不是大于
            if i == len(increase):  # if x 插入位置在最后一个，表示大于维护递增数列最大值，满足升序，直接append
                increase.append(x)
            else:
                # 这一步最关键，不满足则直接替换对应位置数字
                # 这个地方分两种情况，如果increase为空，相当于直接append，如果已经有数字，则替换对应位置数字
                # 比如【2，5】，来了一个3，这个时候变成2，3，其实长度并没有变
                increase[i] = x
        return len(increase)
