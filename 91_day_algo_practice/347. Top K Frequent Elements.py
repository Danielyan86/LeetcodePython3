class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cn = collections.Counter(nums)
        tmp = [x[0] for x in sorted(cn.items(), key=lambda item: item[1], reverse=True)]
        return tmp[:k]


class Solution2:
    count = collections.Counter(nums)
    min_heap = []
    for i in count:
        heapq.heappush(min_heap, (count[i], i))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num[1] for num in min_heap]
