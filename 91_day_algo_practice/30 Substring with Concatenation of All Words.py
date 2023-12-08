from typing import List
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        words_counter = collections.Counter(words)
        word_l = len(words[0])
        words_l = word_l * len(words)
        index = 0
        while index + words_l <= len(s) and index < len(s):
            if s[index : index + word_l] in words_counter:
                tmp_list = [
                    s[j : j + word_l] for j in range(index, index + words_l, word_l)
                ]
                if collections.Counter(tmp_list) == words_counter:
                    res.append(index)
            index += 1
        return res


if __name__ == "__main__":
    s = Solution()
    s.findSubstring("foobarman", ["foo", "bar"])
