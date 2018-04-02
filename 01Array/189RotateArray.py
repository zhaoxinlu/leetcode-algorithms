# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-02
算法思想：旋转数组
"""
class Solution(object):
    def rotate(self, nums, k):
        """
            将前n-k个原地反转，
            将后k个原地反转，
            再将整个数组原地反转，
            即得所求。【时间复杂度O(n)，空间复杂度O(1)】
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverseArr(nums, 0, len(nums)-k-1)
        self.reverseArr(nums, len(nums)-k, len(nums)-1)
        self.reverseArr(nums, 0, len(nums)-1)

    def reverseArr(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotateII(self, nums, k):
        """
        利用python自带的切片特性
        :param nums:
        :param k:
        :return:
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]