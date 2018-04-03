# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-03
算法思想：总结区间--双指针变量
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
            需要两个变量i和j，其中i是连续序列起始数字的位置，j是连续数列的长度，
            当j为1时，说明只有一个数字，若大于1，则是一个连续序列
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        start = 0
        while start < len(nums):
            end = 1
            while start+end < len(nums) and nums[start+end]-nums[start] == end:
                end += 1
            if end == 1:
                result.append(str(nums[start]))
            else:
                result.append(str(nums[start])+'->'+str(nums[start+end-1]))
            start += end

        return result

if __name__ == '__main__':
    nums = [0, 2, 3, 4, 6, 8, 9]
    print Solution().summaryRanges(nums)