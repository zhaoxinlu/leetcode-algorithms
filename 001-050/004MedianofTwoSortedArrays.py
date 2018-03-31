# -*- coding: utf-8 -*-
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        len1 = len(nums1)
        len2 = len(nums2)
        i = j = 0
        while i < len1 and j < len2:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len1:
            nums.append(nums1[i])
            i += 1
        while j < len2:
            nums.append(nums2[j])
            j += 1

        len3 = len(nums)
        if len3 % 2 == 0:
            num = (nums[len3/2-1] + nums[len3/2]) * 1.0 / 2
        else:
            num = nums[(len3-1)/2]
        return num

if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 3], [2, 4])