# 巧妙利用ython collections.default函数 和默认dict最大一个区别是为空的时候不会抛出异常
# 巧妙利用list有序map到26个字母构造字典的key,
# be cause the list is mutable , it can't be used as dictionary key
# after using the list factory fucntion, the dictionary can use the append method to append the item to one dict content easily
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for st in strs:
            # initialize a list with 26 0
            counts = [0] * 26
            for ch in st:
                # in order to map 0 to a, need to miuns the ASCII of a character, then the index 0 is used to record number of 'a'
                counts[ord(ch) - ord("a")] += 1
            # use tuple to make the key is a hash balue
            # if the key doesn't exist in mp, it will be created as a new one, that's why we use collections
            # because we pass the list as factory function, we can use append function here
            mp[tuple(counts)].append(st)

        return list(mp.values())


if __name__ == "__main__":
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s.groupAnagrams(strs)
