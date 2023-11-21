class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        orgin_d, sorted_d = collections.defaultdict(int), collections.defaultdict(int)
        res = 0
        for i, j in zip(arr, sorted(arr)):
            orgin_d[i] = orgin_d[i] + 1
            sorted_d[j] = sorted_d[j] + 1
            if orgin_d == sorted_d:
                res += 1

        return res
