class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len, t_len = len(s), len(t)
        if t_len > s_len:
            return ""

        cnt = collections.Counter(t)  # 统计滑动窗口内需要匹配的字符总数
        need = t_len

        start, end = 0, -1  # 初始化边界, 有可能结果不存在，所以是0到-1
        min_len = s_len + 1
        l = 0

        for r in range(s_len):  # 开始移动右侧边界
            ch = s[r]
            if ch in cnt:  # 是目标字母则计数减一
                if cnt[ch] > 0:  # 如果已经是0了表示某一个字符在窗口内出现次数超过了目标值，不用再递减
                    need -= 1  # need 的值最少也就减少到0
            cnt[ch] -= 1  # cnt每个字符的值可能小于0，因为单位窗口内允许出现超过目标字符

            while need == 0:  # 当计数减为0的时候开始计算当前滑动窗口大小，并开始收缩左侧边界
                if r - l + 1 < min_len:  # 和最小值比较开始更新最小滑动窗口的起点和终点
                    min_len = r - l + 1
                    start, end = l, r
                ch = s[l]
                if ch in cnt:  # 如果不是目标字符，直接滑走
                    if cnt[ch] >= 0:  # 如果是目标字符，则判断是否还有多的，如果没有多的了，则need+1
                        need += 1  # need一旦变化，则下一轮跳出循环
                    cnt[ch] += 1  # 先把小于0的数字恢复，只有大于0了才需要+need
                l += 1
        return s[start : end + 1]
