# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-24
算法思想：下一个排列
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] > nums[idx-1]:
                break

        for i in range(len(nums)-1, idx-1, -1):
            if nums[i] > nums[idx-1]:
                nums[i], nums[idx-1] = nums[idx-1], nums[i]
                break

        tmp = nums[idx:]
        tmp.sort()
        nums[idx:] = tmp

        return nums

if __name__ == '__main__':
    print Solution().nextPermutation([1, 3, 2])