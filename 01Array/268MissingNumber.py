# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-06
算法思想：缺失的数
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        return (length * (length+1)) / 2 - sum(nums)

if __name__ == '__main__':
    nums = [3, 0, 1]
    print Solution().missingNumber(nums)