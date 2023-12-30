class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []
        res = []
        s_cnt = [0] * 26
        p_cnt = [0] * 26
        for i in range(p_len):
            s_cnt[ord(s[i]) - 97] += 1
            p_cnt[ord(p[i]) - 97] += 1
        if s_cnt == p_cnt:
            res.append(0)
        for i in range(len(p), len(s)):
            s_cnt[ord(s[i]) - 97] += 1
            s_cnt[ord(s[i - p_len]) - 97] -= 1
            if s_cnt == p_cnt:
                res.append(i - p_len + 1)
        return res
