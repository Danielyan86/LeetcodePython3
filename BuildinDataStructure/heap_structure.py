import heapq


def find_k_smallest(nums, k):
    return heapq.nsmallest(k, nums)


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k_smallest = find_k_smallest(numbers, 3)
print(k_smallest)


minl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 123123, 1231, 1, 1, 2]
heapq.heapify(minl)
print(minl)
# print(h)


#
