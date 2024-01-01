# 双指针大法
class Solution:
    def trap(self, height: List[int]) -> int:
        # 注意结果是个累加，两个高度有差值就可以接住雨水，
        # 每个值是一个宽度，想像成一个木片，两个木片一样高是接不住的，注意边界值考虑
        # 哪边小计先算那边 ,木桶效应
        res = l = lh_max = rh_max = 0
        r = len(height) - 1
        while l < r:
            # find the higest height of the left
            lh_max = max(lh_max, height[l])
            rh_max = max(rh_max, height[r])
            if lh_max < rh_max:  # 哪边小计先算那边，需要注意是当前当前高度，不是max
                res += lh_max - height[l]  # 用一边最高 - 一遍当前高度，累加到res里面·
                l += 1
            else:
                res += rh_max - height[r]
                r -= 1
        return res
