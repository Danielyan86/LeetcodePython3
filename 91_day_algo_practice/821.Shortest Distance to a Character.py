class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pre = cur = s.find(c)
        res = [0] * len(s)

        for i, st in enumerate(s):
            if st == c and i > cur:
                cur = i
                for mi in range(pre + (cur - pre) // 2 + 1, cur):
                    res[mi] = abs(cur - mi)
                pre = cur
            else:
                res[i] = abs(i - cur)
        return res
