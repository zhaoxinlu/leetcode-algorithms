# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-25
Function: 区域检索--动态规划
"""
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1]-self.dp[i]