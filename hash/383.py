from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranDict, magDict = defaultdict(int), defaultdict(int)
        for s in ransomNote:
            ranDict[s] += ranDict[s]
        for s in magazine:
            magDict[s] += magDict[s]
        for s in ranDict:
            print(s)
            if s not in magDict:
                return False
            print(ranDict[s])
            if ranDict[s] > magDict[s]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    s.canConstruct("aa", "ab")
