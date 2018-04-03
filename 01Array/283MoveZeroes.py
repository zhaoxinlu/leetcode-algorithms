# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：移动0--双指针变量
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] != 0:
                if j != i:
                    nums[i] = nums[j]
                    i += 1
                    nums[j] = 0
                else:
                    i += 1
            j += 1