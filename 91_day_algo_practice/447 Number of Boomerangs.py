class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            hashmap = collections.defaultdict(int)
            for j in range(len(points)):
                distant = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                hashmap[distant] += 1
                res += hashmap[distant] * 2 - 2
        return res
