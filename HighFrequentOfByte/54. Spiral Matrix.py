class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 顺时针打印，不断缩小边界
        if not matrix:
            return matrix
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1):  # 从左往右遍历
                res.append(matrix[t][i])
            t += 1  # 第一层走完，t+1
            if t > b:
                break
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res
