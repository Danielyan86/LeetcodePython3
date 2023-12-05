class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        counter = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i]:
                counter += 1
            else:
                return counter


s = Solution()
s.lengthOfLastWord("hello world")
