# 三个指针，倒序遍历
# 一个指针指向要插入的位置，剩下两个分别指向两个数组有数字的末端
# while判定只考虑第二个数组指针大于0，因为如果第二个数组数字遍历完了之后，不用再次遍历第一个，因为数组本身是有序的
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, k = m - 1, n - 1, m + n - 1
        while p2 >= 0:  # nums2 还有要合并的元素
            # 如果 p1 < 0， 说明第一个数组已经遍历完了，必须加上p1>=0这个判断
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[k] = nums1[p1]
                p1 -= 1
            else:
                nums1[k] = nums2[p2]
                p2 -= 1
            k -= 1
