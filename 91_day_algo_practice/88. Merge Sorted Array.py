# 三个指针，倒序遍历
# 一个指针指向要插入的位置，剩下两个分别指向两个数组有数字的末端
# while判定只考虑第二个数组指针大于0，因为如果第二个数组数字遍历完了之后，不用再次遍历第一个，因为数组本身是有序的
# 第一个判断必须是先移动第一个数组
# 如果 p1 < 0， 说明第一个数组已经遍历完了，必须加上p1>=0这个判断,这样直接走else这个分之，这是这个题最tricky的地方
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2, k = m - 1, n - 1, m + n - 1
        while n2 >= 0:
            if n1 >= 0 and nums1[n1] >= nums2[n2]:
                nums1[k] = nums1[n1]
                n1 -= 1
            else:
                nums1[k] = nums2[n2]
                n2 -= 1
            k -= 1
