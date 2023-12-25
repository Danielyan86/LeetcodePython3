class Solution:
    def trap(self, height: List[int]) -> int:
        res = l = lh_max = rh_max = 0
        r = len(height) - 1
        while l < r:
            # find the higest height of the left
            lh_max = max(lh_max, height[l])
            rh_max = max(rh_max, height[r])
            if lh_max < rh_max:
                res += lh_max - height[l]
                l += 1
            else:
                res += rh_max - height[r]
                r -= 1
        return res
