class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        return str(set(s))


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.removeDuplicateLetters("sdsfds")
    print(res)
