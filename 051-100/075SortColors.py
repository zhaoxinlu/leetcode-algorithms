# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-27
算法思想：颜色排序
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return

        length = len(nums)
        i = 0
        n0 = 0
        n2 = length-1
        while i <= n2:
            if nums[i] == 2:
                nums[i], nums[n2] = nums[n2], nums[i]
                n2 -= 1
            elif nums[i] == 0:
                nums[i], nums[n0] = nums[n0], nums[i]
                n0 += 1
                i += 1
            else:
                i += 1