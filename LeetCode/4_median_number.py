class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        new_list = sorted(nums1)
        length = len(new_list)
        if length % 2 == 0:
            return (new_list[length // 2 - 1] + new_list[length // 2]) / 2
        else:
            return new_list[length // 2]

    def findMedianSortedArrays2(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        imin, imax, half_len = 0, len1, (len1 + len2 + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if i<len1 and


if __name__ == "__main__":
    s_obj = Solution()
    res = s_obj.findMedianSortedArrays([1, 2], [3, 4])
    print(res)
